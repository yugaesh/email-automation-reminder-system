EMAIL AUTOMATION & REMINDER SYSTEM (PYTHON + STREAMLIT)

========================================================

PROJECT OVERVIEW
========================================================
The Email Automation & Reminder System is a Python-based automation project that simulates real-world email workflows used in companies.

It automates repetitive tasks like sending reminders, notifications, and follow-ups using CSV files, email templates, and a Streamlit dashboard.

This project demonstrates backend automation, UI integration, and workflow design.

--------------------------------------------------------

PROBLEM STATEMENT
--------------------------------------------------------
Organizations face problems like:
- Manual email sending
- Missed reminders and follow-ups
- Time-consuming repetitive communication
- No tracking system for emails

This project solves these problems using automation.

--------------------------------------------------------

KEY FEATURES
--------------------------------------------------------
- Automated email sending using SMTP
- CSV-based contact management
- Email template personalization
- DRY RUN mode (safe testing)
- LIVE mode (real email sending)
- Streamlit web dashboard
- Logging system for tracking
- Output report generation

--------------------------------------------------------

TECH STACK
--------------------------------------------------------
- Python
- Pandas
- Streamlit
- SMTP (smtplib)
- email.message
- CSV files
- Logging module

--------------------------------------------------------

PROJECT STRUCTURE
--------------------------------------------------------
Email-Automation-Reminder-System/
│
├── app.py # Streamlit UI dashboard
├── main.py # Backend automation logic
│
├── data/
│ └── contacts.csv # Contact database
│
├── templates/
│ └── email_template.txt # Email template
│
├── logs/
│ └── system.log # Execution logs
│
├── outputs/
│ └── sent_emails.csv # Email status report
│
├── requirements.txt # Dependencies
└── README.md

--------------------------------------------------------

INSTALLATION STEPS
--------------------------------------------------------

1. Clone the repository:
git clone https://github.com/your-username/email-automation-reminder-system.git

2. Go to project folder:
cd email-automation-reminder-system

3. Install dependencies:
pip install -r requirements.txt

--------------------------------------------------------

HOW TO RUN PROJECT
--------------------------------------------------------

1. Run Streamlit Dashboard:
streamlit run app.py

2. (Optional) Run backend script:
python main.py

--------------------------------------------------------

MODES
--------------------------------------------------------

DRY RUN MODE:
- No real emails sent
- Used for testing and debugging
- Safe mode

LIVE MODE:
- Sends real emails using Gmail SMTP
- Requires App Password
- Use carefully

--------------------------------------------------------

WORKFLOW
--------------------------------------------------------
CSV Contacts → Streamlit UI → Email Template →
Automation Engine → SMTP Sender → Logs & Reports

--------------------------------------------------------

SCREENSHOTS TO ADD (IMPORTANT)
--------------------------------------------------------
Take screenshots of:
- Streamlit dashboard UI
- CSV upload screen
- Email output results
- Terminal execution output
- GitHub repository page

--------------------------------------------------------

LEARNING OUTCOMES
--------------------------------------------------------
- Email automation using Python
- SMTP email handling
- CSV file processing
- Streamlit UI development
- Logging and debugging
- Real-world workflow design

--------------------------------------------------------

REAL WORLD USE CASES
--------------------------------------------------------
- HR reminder systems
- Sales follow-up systems
- Payment reminder systems
- Educational notifications
- Marketing automation systems

--------------------------------------------------------

SECURITY NOTE
--------------------------------------------------------
- Never upload real passwords to GitHub
- Use Gmail App Password instead
- Keep DRY RUN mode enabled for testing

--------------------------------------------------------

FUTURE IMPROVEMENTS
--------------------------------------------------------
- Email scheduling system
- Database integration (SQLite/MySQL)
- Authentication system
- Analytics dashboard
- Email tracking (open/click tracking)

--------------------------------------------------------

AUTHOR
--------------------------------------------------------
Yugaesh Kumaran

--------------------------------------------------------

SUMMARY
--------------------------------------------------------
This project is a complete Email Automation System with:
- Backend automation
- UI dashboard
- Safe testing mode
- Real-world workflow simulation

========================================================