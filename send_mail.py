import smtplib
import os
from dotenv import load_dotenv, find_dotenv
from email.mime.text import MIMEText
from email.header import Header

load_dotenv(find_dotenv())


def send_message(message):
    sender = os.getenv("SENDER_EMAIL")
    password = os.getenv("YANDEX_EMAIL_PASSWORD")
    recipient = os.getenv("EMAIL_RECIPIENT")

    msg = MIMEText(message, 'plain', 'utf-8')
    msg["From"] = sender
    msg["Subject"] = Header('New sticker order', 'utf-8')

    server = smtplib.SMTP("smtp.yandex.ru", 587)

    try:
        server.starttls()
        server.login(sender, password)
        server.sendmail(msg["From"], recipient, msg.as_string())
        # return 'OK'
    except Exception as ex:
        return f"{ex}\n Check the data you entered."

    finally:
        server.quit()
