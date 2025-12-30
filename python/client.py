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
    
    def getUsers(self, token):
        point = self.base_url + "users"
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(point, headers=headers, verify=False)
        return response
    
    def getProducts(self, page, per_page):
        point = self.base_url + "products"
        params = {
            "page": page,
            "per_page": per_page
        }
        response = requests.get(point, params=params, verify=False)
        return response
        