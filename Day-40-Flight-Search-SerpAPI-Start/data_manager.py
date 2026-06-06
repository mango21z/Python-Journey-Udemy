import os
import requests
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_PRICES_ENDPOINT"]
SHEETY_USERS_ENDPOINT = os.environ["SHEETY_USERS_ENDPOINT"]
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

class DataManager:

    def __init__(self):
        self.sheety_headers = {
            "Authorization": f"Basic {SHEETY_TOKEN}",
        }
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.sheety_headers
        )

    def get_customer_emails(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.sheety_headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data