import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils import get_job_id, determine_resume, fill_fields, save_job_data
from notifications import send_email
import logging

def login(driver, config, max_retries=3):
    for attempt in range(max_retries):
        try:
            driver.get("https://www.linkedin.com/login")
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "username")))
            email_field = driver.find_element(By.ID, "username")
            email_field.send_keys(config["email"])
            password_field = driver.find_element(By.ID, "password")
            password_field.send_keys(config["password"])
            password_field.send_keys(Keys.RETURN)
            time.sleep(5)
            # Check for CAPTCHA
            if "checkpoint" in driver.current_url or "security verification" in driver.current_url:
                logging.error("CAPTCHA detected during login")
                send_email(config, "LinkedIn Automation: CAPTCHA Detected", "CAPTCHA encountered during login. Please complete it manually and restart.")
                return False
            logging.info("Logged in successfully")
            send_email(config, "LinkedIn Automation: Login Successful", "Successfully logged into LinkedIn.")
            return True
        except (TimeoutException, NoSuchElementException) as e:
            logging.warning(f"Login attempt {attempt+1} failed: {e}")
            if attempt == max_retries - 1:
                logging.error("Max login retries reached")
                send_email(config, "LinkedIn Automation: Login Failed", f"Failed to login after {max_retries} attempts: {e}")
                return False
            time.sleep(5)

def set_filters(driver, max_retries=3):
    for attempt in range(max_retries):
        try:
            driver.get("https://www.linkedin.com/jobs/")
            time.sleep(3)
            date_filter = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Date Posted')]"))
            )
            date_filter.click()
            time.sleep(1)
            past_24 = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Past 24 hours')]"))
            )
            past_24.click()
            time.sleep(1)
            apply_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Show')]"))
            )
            apply_button.click()
            time.sleep(3)
            logging.info("Filters set to past 24 hours")
            return True
        except (TimeoutException, NoSuchElementException) as e:
            logging.warning(f"Filter setting attempt {attempt+1} failed: {e}")
            if attempt == max_retries - 1:
                logging.error("Max filter retries reached")
                send_email(config, "LinkedIn Automation: Filter Error", f"Failed to set filters: {e}")
                return False
            time.sleep(5)

def search_jobs(driver, keyword, max_retries=3):
    for attempt in range(max_retries):
        try:
            search_box = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search jobs']"))
            )
            search_box.clear()
            search_box.send_keys(keyword)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)
            logging.info(f"Searched for jobs with keyword: {keyword}")
            return True
        except (TimeoutException, NoSuchElementException) as e:
            logging.warning(f"Search attempt {attempt+1} for '{keyword}' failed: {e}")
            if attempt == max_retries - 1:
                logging.error(f"Max search retries reached for '{keyword}'")
                send_email(config, "LinkedIn Automation: Search Error", f"Failed to search for '{keyword}': {e}")
                return False
            time.sleep(5)

def apply_to_job(driver, job, config, applied_jobs):
    try:
        job_id = get_job_id(job)
        if job_id in applied_jobs:
            logging.info(f"Skipped already applied job: {job_id}")
            return
        job.click()
        time.sleep(2)
        easy_apply_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'jobs-apply-button')]"))
        )
        if "Easy Apply" not in easy_apply_button.text:
            return
        easy_apply_button.click()
        time.sleep(2)
        if len(driver.window_handles) > 1:
            driver.switch_to.window(driver.window_handles[1])
            if "linkedin.com" not in driver.current_url:
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                logging.info(f"Skipped job {job_id} due to external redirect")
                return
            driver.switch_to.window(driver.window_handles[0])
        job_title = driver.find_element(By.CLASS_NAME, "jobs-unified-top-card__job-title").text
        company = driver.find_element(By.CLASS_NAME, "jobs-unified-top-card__company-name").text
        resume_path = os.path.abspath(determine_resume(job_title, config))
        resume_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )
        resume_input.send_keys(resume_path)
        time.sleep(2)
        application_steps = 0
        while application_steps < 5:
            fill_fields(driver, config)
            try:
                button = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@type='button']"))
                )
                button_text = button.text.lower()
                if "next" in button_text or "continue" in button_text:
                    button.click()
                elif "review" in button_text:
                    button.click()
                elif "submit" in button_text:
                    if not config["dry_run"]:
                        button.click()
                        applied_jobs.add(job_id)
                        save_job_data(job_id, job_title, company, config)
                        logging.info(f"Submitted application for job: {job_title} (ID: {job_id})")
                        send_email(
                            config,
                            "LinkedIn Automation: Job Application Submitted",
                            f"Applied to job: {job_title} at {company} (ID: {job_id})"
                        )
                    else:
                        logging.info(f"Dry run: Would submit application for job: {job_title} (ID: {job_id})")
                    break
                time.sleep(2)
                application_steps += 1
            except:
                break
        try:
            close_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Dismiss']"))
            )
            close_button.click()
            time.sleep(2)
        except:
            pass
    except Exception as e:
        logging.error(f"Error applying to job {job_id}: {e}")
        send_email(config, "LinkedIn Automation: Error", f"Error applying to job {job_id}: {e}")