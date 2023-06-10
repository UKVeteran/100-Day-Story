import requests
from datetime import datetime

USERNAME = "ukveteran"
TOKEN = "THISISTOPSECRET"
GRAPH_ID = "UKV1729"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

