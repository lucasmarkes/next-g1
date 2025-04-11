import requests

url = "http://127.0.0.1:8000/repos"
data = {"owner": "lucasmarkes", "repo": "next-exercicios"}

response = requests.post(url, json=data)
print(response.json())