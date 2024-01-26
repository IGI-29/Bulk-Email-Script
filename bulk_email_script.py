# email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication

# Email configuration
sender_email = "sendersEmail"
subject = "Email Title"
body = """
message body, we can use html tags for styling. For example <b>Bold Text </b> used for bolding the required text.
And <br> breaking the line.
"""

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Gmail SMTP port

# Your email credentials
username = "sendersEmail"
password = "enter the valid password created by smtp server configuration of gmail"

# File containing a list of recipient email addresses, one per line
recipient_file = r'path of the txt file of emails'

# Read the recipient email addresses from the file
with open(recipient_file, 'r') as file:
    recipients = [line.strip() for line in file]

# Loop through the list of recipients and send individual emails
for receiver_email in recipients:
    # Create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "html"))

    attachment_path = r'path of the attachement (resume)'
    attachment_filename = 'Resume_Adarsh.pdf'
    with open(attachment_path, "rb") as attachment:
        pdf_part = MIMEApplication(attachment.read(), _subtype="pdf")
        pdf_part.add_header('Content-Disposition',
                            f'attachment; filename="{attachment_filename}"')
        message.attach(pdf_part)

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Enable TLS encryption

    try:
        server.login(username, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully! to", receiver_email)
    except Exception as e:
        print("An error occurred: ", str(e))
    finally:
        server.quit()
