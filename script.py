import ssl
import smtplib
import maskpass
from email.message import EmailMessage

sender = input('Your email: ')
password = maskpass.askpass(prompt="Enter your Password: ", mask="*") 
receiver = input('Send to: ')
subject = input('Subject: ')
body= input('Body: ')

email = EmailMessage()

email['From'] = sender
email['To'] = receiver
email['subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, email.as_string())