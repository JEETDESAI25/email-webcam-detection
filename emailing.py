import smtplib
import imghdr
import os
from email.message import EmailMessage

PASSWORD = os.getenv("PASSWORD")
SENDER = "jeetdesai25@gmail.com"
RECEIVER = "hetansheeshah@gmail.com"


def send_email(image_path):
    print("send_email function started")
    email_message = EmailMessage()
    email_message["subject"] = "Someone's Here!"
    email_message.set_content("Hey, we just saw a new person!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(
        content, maintype="image", subtype=imghdr.what(None, content)
    )

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send email function ended")


if __name__ == "__main__":
    send_email(image_path="images/19.png")
