import requests
import json

def auth():
    endpoint = "http://127.0.0.1:9100/auth/"
    response = requests.post(endpoint,json={"username":"apiadmin","password":"admin"})
    if response.status_code == 200 :
        token=response
        return token.json()# {'token': '35fd13777168eb84e0e41413fd3f7cda55e7fe3b'}
    return response.status_code

def get():
    token=auth()
    strtoken=(token['token'])
    endpoint = "http://127.0.0.1:9100/softdrinks/home/"
    headers={"Authorization":f"bearer {strtoken}"}
    response = requests.get(endpoint,headers=headers)
    return response.json()

def create():
    headers={"Authorization":"bearer 35fd13777168eb84e0e41413fd3f7cda55e7fe3b"}
    endpoint = "http://127.0.0.1:9100/softdrinks/home/"
    response = requests.post(endpoint,headers=headers,json={
                "brand": " brand #white ass",
                "description": "white as ass",
                "quantity": "750ml",
                "price":25
    })
#
    return response.json()

def detail(pk):
    headers={"Authorization":"bearer 35fd13777168eb84e0e41413fd3f7cda55e7fe3b"}
    endpoint = f"http://127.0.0.1:9100/softdrinks/soda/{pk}/"
    response = requests.get(endpoint,headers=headers)
    return response.json()

def update(pk):
    headers={"Authorization":"bearer 35fd13777168eb84e0e41413fd3f7cda55e7fe3b"}
    endpoint = f"http://127.0.0.1:9100/softdrinks/soda/{pk}/"
    response = requests.put(endpoint,headers=headers,json={
                "brand": "new fanta ",
                "description": "black as ass",
                "quantity": "750ml",
                "price":250
    })
    return response.json()



#print(auth())

#print(get())

print(detail(1))

#print(update(1))

#print(create())