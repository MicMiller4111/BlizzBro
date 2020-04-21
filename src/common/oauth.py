import requests
from requests.auth import HTTPBasicAuth
import json

with open("wowcreds.json") as creds:
    creds = json.load(creds)

class Oauth:
    def getToken():
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post("https://us.battle.net/oauth/token", 
            auth=HTTPBasicAuth(creds["client_id"], creds["secret"]), 
            data="grant_type=client_credentials",
            headers=headers)
        res = json.loads(response.content)
        token = res["access_token"]
        return token