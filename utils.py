import os
import pandas as pd
from datetime import datetime
from selenium.webdriver.common.by import By

def get_job_id(job):
    try:
        link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
        job_id = link.split('/view/')[1].split('/')[0]
        return job_id
    except:
        return None

def determine_resume(job_title, config):
    job_title = job_title.lower()
    for keyword, resume_path in config["resume_mapping"].items():
        if keyword in job_title:
            return resume_path
    return "resumes/default_resume.pdf"

def match_question_to_answer(question_text, config):
    question_text = question_text.lower().strip()
    for key, answer in config["answers"].items():
        if key in question_text:
            return answer
    return None

def fill_field(element, answer):
    if element.tag_name == "input":
        input_type = element.get_attribute("type")
        if input_type in ["text", "email", "tel"] and not element.get_attribute("value"):
            element.send_keys(answer)
        elif input_type == "radio" and answer.lower() in element.get_attribute("value").lower():
            element.click()
        elif input_type == "checkbox" and answer.lower() == "yes":
            element.click()
    elif element.tag_name == "select":
        from selenium.webdriver.support.ui import Select
        Select(element).select_by_visible_text(answer)
    elif element.tag_name == "textarea" and not element.get_attribute("value"):
        element.send_keys(answer)

def fill_fields(driver, config):
    labels = driver.find_elements(By.TAG_NAME, "label")
    for label in labels:
        label_text = label.text.lower().strip()
        for_attr = label.get_attribute("for")
        answer = match_question_to_answer(label_text, config)
        if for_attr and answer:
            try:
                element = driver.find_element(By.ID, for_attr)
                fill_field(element, answer)
            except:
                continue

def save_job_data(job_id, job_title, company, config):
    data = {
        "job_id": job_id,
        "job_title": job_title,
        "company": company,
        "date_applied": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.DataFrame([data])
    csv_file = config["data_tracking"]["csv_file"]
    if os.path.exists(csv_file):
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        df.to_csv(csv_file, mode='w', header=True, index=False)
    os.makedirs('artifacts', exist_ok=True)
    df.to_csv('artifacts/job_data.csv', mode='a', header=not os.path.exists('artifacts/job_data.csv'), index=False)