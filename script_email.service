import smtplib
from email.message import EmailMessage
import os

msg = EmailMessage()
msg['From'] = "[email protected]"
msg['To'] = "[email protected]"
msg['Subject'] = "Fisier atasat"
msg.set_content("Fisierul a fost trimis automat.")

with open("/home/test1/Desktop/test/rezultat.txt", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename="rezultat.txt")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login("[email protected]", os.environ.get("EMAIL_PASSWORD"))
    server.send_message(msg)

print("Trimis!")
