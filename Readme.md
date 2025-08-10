Email Sender Script
This Python script sends multiple emails to a specified recipient using the smtplib library and Ethereal Email's SMTP server.
Prerequisites

Python 3.x
Required libraries: smtplib, email.mime.text, email.mime.multipart
An Ethereal Email account (or another SMTP server account)

Setup

Install Python: Ensure Python 3.x is installed on your system.
Obtain SMTP Credentials:
Sign up at Ethereal Email to get a temporary email and password for testing.
Alternatively, use your own SMTP server details (e.g., Gmail, Outlook).


Configure the Script:
Open the script and update the following variables in the CONFIGURE THESE section:
SENDER_EMAIL: Your email address (e.g., your-email@ethereal.email).
SENDER_PASSWORD: Your email account password.
SMTP_SERVER: The SMTP server address (e.g., smtp.ethereal.email).
SMTP_PORT: The SMTP server port (e.g., 587 for TLS).
RECEIVER_EMAIL: The recipient's email address.
NUMBER_OF_EMAILS: Number of emails to send.
DELAY_SECONDS: Delay between emails in seconds.


Customize the SUBJECT and BODY variables in the EMAIL CONTENT section as needed.



Usage

Save the script as send_emails.py.
Run the script using:python send_emails.py


The script will:
Connect to the SMTP server.
Send the specified number of emails with the defined subject and body.
Wait for the specified delay between each email.
Display progress and any errors.



Example Output
✅ Logged in to SMTP server successfully.
📤 Email 1 sent successfully.
⏳ Waiting 3 seconds...
📤 Email 2 sent successfully.
...
✅ All emails sent successfully!

Notes

Ethereal Email: This service is for testing purposes only. Emails are not delivered to real inboxes but can be viewed in the Ethereal Email dashboard.
Security: Avoid hardcoding sensitive credentials in the script for production use. Use environment variables or a configuration file instead.
Error Handling: The script includes basic error handling to catch and display issues like authentication failures or server connection problems.

Troubleshooting

Authentication Error: Verify SENDER_EMAIL and SENDER_PASSWORD.
Connection Issues: Check SMTP_SERVER and SMTP_PORT. Ensure your network allows connections to the SMTP server.
No Emails Received: If using Ethereal Email, check the dashboard at ethereal.email. For other services, verify the recipient's email and server settings.
