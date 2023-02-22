from django.shortcuts import render

# Create your views here.
import requests

endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint)

print(response.json())