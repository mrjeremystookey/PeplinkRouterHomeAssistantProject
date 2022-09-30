import requests
import json
import urllib3

print("\n************PepLinkRouterProject************")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

params = ""

username = "admin"
password = "Acadia516!"

loginData = {
    "username": f"{username}",
    "password": f"{password}"
}

hostname = 'https://192.168.50.1'
login_url = '/api/login'


def login():
    print(f'\nattempting to login to local Pepwave router at {hostname + login_url}\n')
    print(f'login data: {loginData}\n')
    urllib3.disable_warnings()
    s = requests.session()
    resp = s.post(url=hostname + login_url,
                  headers=headers,
                  data=json.dumps(loginData),
                  json=loginData,
                  verify=False)
    print(f"returned json: {resp.json()}\n")
    if resp.status_code != 200:
        print('error: ' + str(resp.status_code))
    else:
        print('Success')


if __name__ == '__main__':
    login()
    print("************PepLinkRouterProject************")
