from fastapi import APIRouter, Depends, HTTPException
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from config import sender_email, yandex_mail_password, recipient_email


router = APIRouter(
    prefix='/send_mail',
    tags=['Send mail']
)


@router.get('')
async def send_message(message):
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
    except Exception:
        raise HTTPException(status_code=500)

    finally:
        server.quit()
