"""
Pixela API Example Project
--------------------------
Creator: Param Sangani

This script demonstrates how to:
1. Create a user
2. Create a graph
3. Add (POST) a pixel
4. Update (PUT) a pixel
5. Delete a pixel

Docs: https://docs.pixe.la
"""

import requests
from datetime import datetime

# --------------------
# Configuration
# --------------------
USERNAME = "your_username_here"   # e.g., "josh123"
TOKEN = "your_token_here"         # e.g., "abc123xyz"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
HEADERS = {"X-USER-TOKEN": TOKEN}


# --------------------
# Create User
# --------------------
def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print("Create User:", response.text)


# --------------------
# Create Graph
# --------------------
def create_graph():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "km",
        "type": "float",
        "color": "ajisai"
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print("Create Graph:", response.text)


# --------------------
# Add Pixel
# --------------------
def add_pixel(quantity: float):
    today = datetime.now().strftime("%Y%m%d")
    pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today,
        "quantity": str(quantity),
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=HEADERS)
    print("Add Pixel:", response.text)


# --------------------
# Update Pixel
# --------------------
def update_pixel(quantity: float):
    today = datetime.now().strftime("%Y%m%d")
    update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    update_data = {"quantity": str(quantity)}
    response = requests.put(url=update_endpoint, json=update_data, headers=HEADERS)
    print("Update Pixel:", response.text)


# --------------------
# Delete Pixel
# --------------------
def delete_pixel():
    today = datetime.now().strftime("%Y%m%d")
    delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    response = requests.delete(url=delete_endpoint, headers=HEADERS)
    print("Delete Pixel:", response.text)


# --------------------
# Main Runner
# --------------------
if __name__ == "__main__":
    # Uncomment the operations you want to run
    create_user()
    # create_graph()
    # add_pixel(9.74)
    # update_pixel(10.2)
    # delete_pixel()

