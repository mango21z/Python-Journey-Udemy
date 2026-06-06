from datetime import datetime
import pandas as pd
import random
import smtplib

my_email = "andreluison99@gmail.com"
password = "yzsp bwwn lfnd oorx"

today = datetime.now()
today_tuple = (today.month, today.day)


data = pd.read_csv('birthdays.csv')

birthday_dict = {(data_row.Month, data_row.Day):data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        content = f.read()
        content = content.replace("[NAME]",birthday_person.Name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person.Email,
            msg=f"Subject: Happy Birthday {birthday_person.Name}\n\n{content}")







