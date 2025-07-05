import logging
import os
import time
import subprocess
import sys
import schedule
import pandas as pd
import pkg_resources
from config import load_config
from webdriver_utils import get_driver
from linkedin_actions import login, set_filters, search_jobs, apply_to_job
from notifications import send_email
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Set up logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    filename='logs/application.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Install dependencies
def install_requirements():
    logging.info("Checking and installing dependencies from requirements.txt")
    required = {}
    with open('requirements.txt', 'r') as f:
        for line in f:
            pkg = line.strip().split('==')[0]
            version = line.strip().split('==')[-1] if '==' in line else None
            required[pkg] = version
    installed = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    
    for pkg, version in required.items():
        if pkg not in installed or (version and installed[pkg] != version):
            logging.info(f"Installing {pkg}=={version}")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", f"{pkg}=={version}"])
            except subprocess.CalledProcessError as e:
                logging.error(f"Failed to install {pkg}: {e}")
                sys.exit(1)
    logging.info("All dependencies installed successfully")

# Load configuration
config = load_config()

# Load applied job IDs
applied_jobs_file = 'applied_jobs.txt'
if os.path.exists(applied_jobs_file):
    with open(applied_jobs_file, 'r') as f:
        applied_jobs = set(f.read().splitlines())
else:
    applied_jobs = set()

def run_job_search():
    driver = get_driver()
    try:
        if not login(driver, config):
            logging.error("Job search cycle aborted due to login failure")
            return
        if not set_filters(driver):
            logging.error("Job search cycle aborted due to filter failure")
            return
        for keyword in config["job_keywords"]:
            if not search_jobs(driver, keyword):
                logging.warning(f"Skipping keyword '{keyword}' due to search failure")
                continue
            applications = 0
            page = 1
            while page <= 5 and applications < config["max_applications"]:
                try:
                    job_cards = WebDriverWait(driver, 15).until(
                        EC.presence_of_all_elements_located((By.CLASS_NAME, "job-card-container"))
                    )
                    for job in job_cards:
                        if applications >= config["max_applications"]:
                            break
                        apply_to_job(driver, job, config, applied_jobs)
                        applications += 1
                    try:
                        next_button = WebDriverWait(driver, 15).until(
                            EC.element_to_be_clickable((By.XPATH, f"//button[@aria-label='Page {page+1}']"))
                        )
                        next_button.click()
                        time.sleep(5)
                        page += 1
                    except TimeoutException:
                        logging.info(f"No more pages for keyword '{keyword}'")
                        break
                except TimeoutException as e:
                    logging.warning(f"Failed to load job cards for '{keyword}': {e}")
                    break
    except Exception as e:
        logging.error(f"Error in job search cycle: {e}")
        send_email(config, "LinkedIn Automation: Cycle Error", f"Error in job search cycle: {e}")
    finally:
        time.sleep(5)  # Delay quit for debugging
        driver.quit()
        logging.info("Job search cycle completed")

def main():
    install_requirements()
    try:
        subprocess.Popen(["streamlit", "run", "frontend.py", "--server.port", str(config["frontend"]["port"])])
        logging.info(f"Streamlit frontend started on port {config['frontend']['port']}")
    except Exception as e:
        logging.error(f"Failed to start Streamlit: {e}")
        send_email(config, "LinkedIn Automation: Streamlit Error", f"Failed to start Streamlit: {e}")
    
    schedule.every(config["schedule"]["interval_minutes"]).minutes.do(run_job_search)
    logging.info(f"Scheduled job search every {config['schedule']['interval_minutes']} minutes")
    run_job_search()
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()