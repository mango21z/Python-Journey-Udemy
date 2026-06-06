import random
import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
load_dotenv()

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD")



now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(now.weekday())

date_of_birth = dt.datetime(year=2003, month=2, day=6)
print(date_of_birth)

with open('quotes.txt', 'r') as f:
    quotes = f.readlines()
if now.weekday() == 4:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="bigmangoseed@gmail.com",
            msg=f"Subject: Motivational Monday\n\n{random.choice(quotes)}"
        )