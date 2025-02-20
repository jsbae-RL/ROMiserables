import requests

url = "http://127.0.0.1:8000/items/5"
data = {
    "name": "Laptop",
    "price": 1500.99,
    "is_offer": True
}

response = requests.put(url, json=data)
print(response.json())  # Print the response JSON