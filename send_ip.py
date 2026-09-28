import smtplib
from email.message import EmailMessage

server_ip = "192.168.10.197"

msg = EmailMessage()
msg["Subject"] = "Python Application URL"
msg["From"] = "avikashr093@gmail.com"
msg["To"] = ""

msg.set_content(
    f"""
Application URL:
https://{server_ip}

Server IP:
{server_ip}

Application:
Multiplication Tables 2 to 10
"""
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(
        "avikashr093@gmail.com",
        ""
    )
    smtp.send_message(msg)

print("Email sent successfully")
