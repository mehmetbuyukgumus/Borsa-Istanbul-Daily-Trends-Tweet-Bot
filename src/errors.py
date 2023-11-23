import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path= "infos.env")
tomailadress = os.getenv("toMailAdress")
frommailadress = os.getenv("fromMailAdress")
mailpassword = os.getenv("mailPassword")


def send_email(body):
    subject = "Code Error"
    sender = frommailadress
    recipients = tomailadress
    password = mailpassword
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipients
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())


