import requests

customer = ["Congratulations! You won a free iPhone!"]
url = 'http://localhost:9696/predict'
response = requests.post(url, json=customer)
result = response.json()
print(result)