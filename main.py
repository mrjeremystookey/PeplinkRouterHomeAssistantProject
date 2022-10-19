import json

import requests
import urllib3

import config

print("\n************PepLinkRouterProject************")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

params = ""

username = config.username
password = config.password

loginData = {
    "username": f"{username}",
    "password": f"{password}"
}

hostname = 'https://192.168.50.1/api/'
login_url = 'login'
connection_status_url = 'status.wan.connection'
create_client_url = 'auth.client'
location_url = 'info.location'

s = requests.sessions.session()


def login():
    print(f'\nattempting to login to local Pepwave router at {hostname + login_url}\n')
    print(f'login data: {loginData}\n')
    urllib3.disable_warnings()
    resp = s.post(url=hostname + login_url,
                  headers=headers,
                  data=json.dumps(loginData),
                  verify=False)
    if resp.status_code != 200:
        print('error: ' + str(resp.status_code))
    else:
        print('Success. Logged in')
        # check_status()
        # create_client()
        get_location()


def create_client():
    print("creating new client for access token")
    new_client_json = {
        "name": "PythonClient",
        "scope": "api",
    }
    resp = s.post(url=hostname + create_client_url,
                  headers=headers,
                  json=new_client_json,
                  verify=False)
    print(f'\n{resp.json()}\n')
    print(f'token: \n{resp.json()["token"]}\n')


def check_status():
    print("\nchecking WAN connection status")
    resp = s.get(url=hostname + connection_status_url,
                 headers=headers,
                 verify=False)
    print(f'\n{resp.json()}\n')


# how to send this to HomeAssistant
def get_location():
    resp = s.get(url=hostname + location_url,
                 headers=headers,
                 verify=False)
    print(f'\n{resp.json()}\n')


if __name__ == '__main__':
    login()
    print("************PepLinkRouterProject************")
