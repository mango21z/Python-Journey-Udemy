import requests
import requests_cache
import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
SHEETY_ENDPOINT = "https://api.sheety.co/bb0a80044f9bdbff20bd0a700837e4b9/copyOfFlightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_headers = {
            "Authorization": f"Basic {SHEETY_TOKEN}",
        }

    def read_sheet(self):
        # requests_cache.install_cache('my_cache', expire_after=3000)
        self.response = requests.get(SHEETY_ENDPOINT, headers=self.sheety_headers)
        self.response.raise_for_status()
        return self.response.json()["prices"]

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price" : {
                "lowestPrice" : new_price,
            }
        }
        requests.put(
            url=f"{SHEETY_ENDPOINT}/{row_id}",
            json=new_data,
            headers=self.sheety_headers,
        )
