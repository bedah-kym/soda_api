import requests

endpoint1 = "https://httpbin.org/anything"
endpoint2 = "http://127.0.0.1:9100/softdrinks/home/"

response = requests.post(endpoint2,json={
            "brand": "sapa",
            "description": "black",
            "quantity": "750ml",
            "price": 3500
 })

print(response.json())
