import requests

def fetch_random_user_free_api():
    url  = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    print(response.status_code)
    if data["success"] and "data" in data:
        user_data  = data["data"]
        print(user_data["login"]["username"])

fetch_random_user_free_api()