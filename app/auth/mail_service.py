import os
from dotenv import load_dotenv

from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT")),
    MAIL_SERVER=os.getenv("MAIL_SERVER"),
    MAIL_STARTTLS=os.getenv("MAIL_STARTTLS") == "True",
    MAIL_SSL_TLS=os.getenv("MAIL_SSL_TLS") == "True"
)
print(conf)


async def send_reset_email(email, token):
    reset_link = f"http://localhost:5173/reset-password?token={token}"
    message = MessageSchema(
        subject="Reset Your Password",
        recipients=[email],
        body=f"<p>Click the link to reset your password: <a href='{reset_link}'>Reset Password</a></p>",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)

    print(f"Reset email sent to {email} with token {token}") 
