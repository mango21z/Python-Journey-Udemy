import requests
import random

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": random.randint(1,20),
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
