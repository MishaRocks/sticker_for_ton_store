import smtplib
from email.mime.text import MIMEText
from email.header import Header

from src.mail.config import sender_email, yandex_mail_password, recipient_email


def send_message(message: str):
    sender = sender_email
    password = yandex_mail_password
    recipient = recipient_email

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
