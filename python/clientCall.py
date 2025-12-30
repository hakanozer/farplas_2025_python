from client import APIClient

api = APIClient()
response = api.login("hakanozer02@gmail.com", "123456")
if response.status_code == 200:
    token = response.json().get("data").get("access_token")  
    print("Login successful. Access token:", token)    
else:
    print("Login failed with status code:", response.status_code)