import os
import requests
from dotenv import load_dotenv

load_dotenv()

MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
MAILGUN_BASE_URL = os.getenv("MAILGUN_BASE_URL")
FROM_EMAIL = os.getenv("FROM_EMAIL")

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
