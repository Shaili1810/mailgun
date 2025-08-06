# main.py
from fastapi import FastAPI, HTTPException
from model import EmailRequest
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

def send_simple_message(to: str, subject: str, message: str):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox21b2f2814339476ca2c22bd9758b85c0.mailgun.org/messages",
        auth=("api", os.getenv('MAILGUN_API_KEY', 'MAILGUN_API_KEY')),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox21b2f2814339476ca2c22bd9758b85c0.mailgun.org>",
            "to": to,
            "subject": subject,
            "text": message
        }
    )

@app.post("/send-email/")
def send_email_api(request: EmailRequest):
    res = send_simple_message(request.to, request.subject, request.message)
    if res.status_code == 200:
        return {"status": "success", "message": "Email sent successfully!"}
    else:
        raise HTTPException(status_code=500, detail=res.text)
