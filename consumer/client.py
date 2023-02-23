import requests
import json

def get():
    endpoint = "http://127.0.0.1:9100/softdrinks/home/"
    response = requests.get(endpoint)
    return response.json()

def create():
    endpoint = "http://127.0.0.1:9100/softdrinks/home/"
    response = requests.post(endpoint,json={
                "brand": " white ass",
                "description": "white as ass",
                "quantity": "750ml",
                "price":250
    })

    return response.json()

def detail(pk):
    endpoint = f"http://127.0.0.1:9100/softdrinks/soda/{pk}/"
    response = requests.get(endpoint)
    return response.json()

def update(pk):
    endpoint = f"http://127.0.0.1:9100/softdrinks/soda/{pk}/"
    response = requests.put(endpoint,json={
                "brand": "new fanta ",
                "description": "black as ass",
                "quantity": "750ml",
                "price":250
    })
    return response.json()

#print(get())

#print(detail(1))

#print(update(1))

print(create())