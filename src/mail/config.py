import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


sender_email = os.getenv("SENDER_EMAIL")
yandex_mail_password = os.getenv("YANDEX_EMAIL_PASSWORD")
recipient_email = os.getenv("EMAIL_RECIPIENT")
