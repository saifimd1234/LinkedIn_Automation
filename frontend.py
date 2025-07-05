import streamlit as st
import pandas as pd
import os
import subprocess
from config import load_config

def run_automation():
    subprocess.Popen(["python", "main.py"])

st.title("LinkedIn Job Application Automation")
config = load_config()

if os.path.exists('artifacts/job_data.csv'):
    df = pd.read_csv('artifacts/job_data.csv')
    st.subheader("Applied Jobs")
    st.dataframe(df)
else:
    st.write("No jobs applied yet.")

st.subheader("Configure Job Search")
keywords = st.text_input("Job Keywords (comma-separated)", ",".join(config["job_keywords"]))
max_applications = st.number_input("Max Applications per Run", min_value=1, value=config["max_applications"])
dry_run = st.checkbox("Dry Run (Simulate without submitting)", value=config["dry_run"])

if st.button("Update Configuration"):
    config["job_keywords"] = [k.strip() for k in keywords.split(",")]
    config["max_applications"] = max_applications
    config["dry_run"] = dry_run
    with open('config.json', 'w') as f:
        import json
        json.dump(config, f, indent=2)
    st.success("Configuration updated!")

if st.button("Start Automation"):
    st.write("Starting automation in the background...")
    run_automation()

if st.button("Stop Automation"):
    st.warning("Stop functionality not implemented. Please terminate the main.py process manually.")