import requests


user_message = "Can you tell me about black holes in 3-4 lines"

request_message = {"message": user_message}

url = "http://localhost:5678/webhook-test/fdc8ccb5-1d2b-4393-9fb7-ca6f2bd2560c"

response = requests.post(url, json=request_message)

print(response.status_code)

print(response.json()[0]["output"])