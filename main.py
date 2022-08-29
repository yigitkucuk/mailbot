import smtplib
import ssl
from email.message import EmailMessage

email_sender = open('email_sender.js', 'r').read()
email_password = open('email_password.js', 'r').read()
email_receiver = open('email_receiver.js', 'r').read()
email_receiver2 = open('email_receiver2.js', 'r').read()

subject = 'This is email subject'
body = """
This is email body
"""

recipients = [email_receiver, email_receiver2]

em = EmailMessage()
em['From'] = email_sender
em['To'] = ", ".join(recipients)
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('asmtp.bilkent.edu.tr', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, recipients, em.as_string())
