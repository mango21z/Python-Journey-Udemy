import requests
from datetime import datetime
import os

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

APP_URL ="https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_URL="https://api.sheety.co/bb0a80044f9bdbff20bd0a700837e4b9/copyOfMyWorkouts/workouts"
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")



app_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

data = {
    "query": "swim for 5 hours",
}

today = datetime.now()

response = requests.post(APP_URL, json=data, headers=app_headers)
result = response.json()["exercises"][0]

print(result)

insert_data = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": result["name"],
        "duration": result["duration_min"],
        "calories": result["nf_calories"],
    }
}


response = requests.post(SHEETY_URL, json=insert_data, auth=(SHEETY_USERNAME, SHEETY_PASSWORD))
response.raise_for_status()


