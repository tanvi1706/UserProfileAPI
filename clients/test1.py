import requests
def client():
    token_h = "Token 29be1dd46939e6eef50cb470c1db799fb5218747"
    # credentials = {
    #     "username": "rose",
    #     "password": "hurt925"
    # }
    
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles", headers=headers)
    print("Status Code:", response.status_code)
    response_data = response.json()
    print(response_data)

if __name__ == "__main__":
    client()