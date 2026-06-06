import smtplib
import os
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

class NotificationManager:
    def __init__(self):
        pass
    #This class is responsible for sending notifications with the deal flight details.
    def send_email(self, message_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=message_body.encode("utf-8"),
            )
        print("email sent")