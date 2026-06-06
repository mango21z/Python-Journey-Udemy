import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os

USERNAME = os.getenv("USERNAME")
TOKEN = os.getenv("TOKEN")
GRAPH_ID = os.getenv("GRAPH_ID")

pixela_endpoint = "https://pixe.la/v1/users"
user_param = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_param)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id" : "graph1",
#     "name": "Running Graph",
#     "unit" : "Km",
#     "type" : "float",
#     "color" : "ajisai",
# }
#
# headers = {
#     "X-USER-TOKEN" : TOKEN,
# }
#
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#input data to pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

graph_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "12",
}

headers = {
    "X-USER-TOKEN" : TOKEN,
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#change data in pixela

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


new_pixel_data = {
    "quantity" : "8",
}

# response = requests.put(graph_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
#
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

response = requests.put(delete_endpoint, json=graph_config, headers=headers)
print(response.text)



