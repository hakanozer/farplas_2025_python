from client import APIClient

api = APIClient()
token = ''
response = api.login("hakanozer02@gmail.com", "123456")
if response.status_code == 200:
    token = response.json().get("data").get("access_token")
else:
    print("Login failed with status code:", response.status_code)

if token != '':
    usersResponse = api.getUsers(token)
    if usersResponse.status_code == 200:
        users = usersResponse.json().get("data")
        print("Users:", users)
    else:
        print("Failed to retrieve users with status code:", usersResponse.status_code)

productsResponse = api.getProducts(1, 10)
if productsResponse.status_code == 200:
    proResponse = productsResponse.json()
    print("Products:", proResponse)
else:
    print("Failed to retrieve products with status code:", productsResponse.status_code)