#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from dotenv import load_dotenv
from pprint import pprint
from datetime import datetime, timedelta

from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

load_dotenv()


flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.read_sheet()

today = datetime.now()
tomorrow = today + timedelta(days=1)
six_month_from_now = today + timedelta(days=(30*6))

flights = flight_search.check_flights("LHR", "CDG", tomorrow, six_month_from_now)
# pprint(flights)

cheapest_flight = find_cheapest_flight(flights, six_month_from_now.strftime("%Y-%m-%d"))
pprint(f"{sheet_data[0]['city']} : GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]['lowestPrice']:
    pprint(f"lower price flight found to {sheet_data[0]['city']}")
    data_manager.update_lowest_price(sheet_data[0]['id'], cheapest_flight.price)
    notification_manager.send_email(message_body=f"Subject: Low price alert! Only GBP {cheapest_flight.price} to fly\n\n"
                                                 f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                                                 f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
else:
    print(f"No email sent. Current price (£{cheapest_flight.price}) is higher than or equal to the sheet price (£{sheet_data[0]['lowestPrice']}).")