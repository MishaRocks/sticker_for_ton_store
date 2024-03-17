from fastapi import FastAPI

from mail.send_mail import send_message
from mail.router import router as mail_router

app = FastAPI(
    title="Sticker for TON store"
)
