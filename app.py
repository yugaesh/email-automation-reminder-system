import streamlit as st
import pandas as pd
import smtplib
from email.message import EmailMessage
from datetime import datetime

# ---------------- CONFIG ----------------
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"

# ---------------- MODE ----------------
st.title("📧 Email Automation & Reminder System")

mode = st.selectbox("Select Mode", ["DRY_RUN", "LIVE"])

# ---------------- FILE UPLOAD ----------------
uploaded_file = st.file_uploader("Upload Contacts CSV", type=["csv"])

# ---------------- TEMPLATE ----------------
template = st.text_area(
    "Email Template",
    "Hello {name},\n\nThis is your reminder email.\n\nRegards,\nAutomation System"
)

# ---------------- EMAIL FUNCTION ----------------
def send_email(to_email, subject, body):
    if mode == "DRY_RUN":
        return f"[DRY RUN] Email to {to_email}"

    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    return f"Sent to {to_email}"

# ---------------- MAIN ACTION ----------------
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Contacts Preview")
    st.dataframe(df)

    if st.button("🚀 Send Emails"):
        results = []

        for _, row in df.iterrows():
            name = row["name"]
            email = row["email"]

            body = template.replace("{name}", name)
            subject = "Reminder Notification"

            result = send_email(email, subject, body)

            results.append({
                "email": email,
                "status": result,
                "time": datetime.now()
            })

            st.write(result)

        st.success("Email process completed!")

        st.write("### Results")
        st.dataframe(pd.DataFrame(results))