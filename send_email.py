import smtplib
from email.message import EmailMessage
import ssl
import os

SENDER_EMAIL = os.environ["SENDER_EMAIL"]
APP_PASSWORD = os.environ["APP_PASSWORD"]
RECEIVER_EMAIL = os.environ["RECEIVER_EMAIL"]

def send_email():
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = "Scheduled Email with QR Code"

    msg.set_content("Hello,\n\nHope you read this.\n")

    with open("qrcode.png", "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="image",
            subtype="png",
            filename="qrcode.png"
        )

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

if __name__ == "__main__":
    send_email()
