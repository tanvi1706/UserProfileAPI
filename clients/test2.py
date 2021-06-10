import requests
def client():
    token_h = "Token 33724b4b649a15c1565ace9a177ae37e5290de3c"
    # data = {
    #     "username": "client2tst",
    #     "email": "test2@rest.edu",
    #     "password1": "changeme123",
    #     "password2": "changeme123",
    # }
    # response = requests.post('http://127.0.0.1:8000/api/rest-auth/registration/', data=data)
    headers = {'Authorization': token_h}
    response = requests.get('http://127.0.0.1:8000/api/profiles/',headers=headers)
    print('Status Code:', response.status_code)
    repsonse_data = response.json()
    print(repsonse_data)

if __name__ == "__main__":
    client()
