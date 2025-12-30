import requests

class APIClient:

    def __init__(self):
        self.base_url = "https://jsonbulut.com/api/"

    def login(self, email, password):
        point = self.base_url + "auth/login"  
        params = {
            "email": email,
            "password": password
        }
        response = requests.post(point, json=params, verify=False)
        return response