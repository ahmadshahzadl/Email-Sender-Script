import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ===== CONFIGURE THESE =====
SENDER_EMAIL = "your-email@ethereal.email"
SENDER_PASSWORD = "your-password"
SMTP_SERVER = "smtp.ethereal.email"
SMTP_PORT = 587
RECEIVER_EMAIL = "receiver@example.com"
NUMBER_OF_EMAILS = 10  # set desired count
DELAY_SECONDS = 3      # seconds between emails

# ===== EMAIL CONTENT =====
SUBJECT = "Subject"
BODY = (
    "Mesage to be Sent."
)

try:
    # Connect to SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("✅ Logged in to SMTP server successfully.")

    for i in range(1, NUMBER_OF_EMAILS + 1):
        message = MIMEMultipart()
        message["From"] = SENDER_EMAIL
        message["To"] = RECEIVER_EMAIL
        message["Subject"] = SUBJECT
        message.attach(MIMEText(BODY, "plain"))

        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        print(f"📤 Email {i} sent successfully.")

        if i < NUMBER_OF_EMAILS:
            print(f"⏳ Waiting {DELAY_SECONDS} seconds...")
            time.sleep(DELAY_SECONDS)

    server.quit()
    print("✅ All emails sent successfully!")

except Exception as e:
    print(f"❌ Error: {e}")
