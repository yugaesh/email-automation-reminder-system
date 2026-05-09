import pandas as pd
import smtplib
from email.message import EmailMessage
import logging
from datetime import datetime
import os

# ---------------- LOGGING SETUP ----------------
logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# ---------------- EMAIL CONFIG ----------------
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"

# ---------------- SAFE MODE (IMPORTANT) ----------------
# True = NO REAL EMAIL SENT (recommended for testing)
# False = REAL EMAIL SENDING
MODE = "DRY_RUN"   # options: DRY_RUN or LIVE

# ---------------- LOAD CONTACTS ----------------
contacts = pd.read_csv("data/contacts.csv")

# ---------------- LOAD TEMPLATE ----------------
def load_template(name):
    with open("templates/email_template.txt", "r") as file:
        template = file.read()
    return template.replace("{name}", name)

# ---------------- EMAIL FUNCTION ----------------
def send_email(to_email, subject, body):
    try:
        # ---------------- DRY RUN MODE ----------------
        if MODE == "DRY_RUN":
            print(f"[DRY RUN] Email to: {to_email}")
            print("Subject:", subject)
            print("Body:", body)
            logging.info(f"DRY RUN email for {to_email}")
            return "Dry-Run Success"

        # ---------------- LIVE MODE ----------------
        msg = EmailMessage()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        logging.info(f"Sent email to {to_email}")
        return "Sent"

    except Exception as e:
        logging.error(f"Failed email to {to_email}: {e}")
        return "Failed"

# ---------------- MAIN EXECUTION ----------------
def run_job():
    print("\n===== EMAIL AUTOMATION SYSTEM STARTED =====\n")

    for _, row in contacts.iterrows():
        name = row["name"]
        email = row["email"]

        subject = "Reminder Notification"
        body = load_template(name)

        status = send_email(email, subject, body)

        # Save output log
        with open("outputs/sent_emails.csv", "a") as f:
            f.write(f"{email},{status},{datetime.now()}\n")

        print(f"{email} -> {status}")

    print("\n===== JOB COMPLETED =====\n")

# ---------------- START PROGRAM ----------------
run_job()