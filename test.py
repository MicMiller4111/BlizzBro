import requests
from requests.auth import HTTPBasicAuth
import json

base_url = 'https://us.api.blizzard.com'
#curl -u {client_id}:{client_secret} -d grant_type=client_credentials https://us.battle.net/oauth/token
def getToken():
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post('https://us.battle.net/oauth/token', 
        auth=HTTPBasicAuth('d6429f6bb04d4cbd8ff044e171bd7fb6', 'J6s6zYMNnsOlJK3Rpz8oBq4P2IVPK5XQ'), 
        data='grant_type=client_credentials',
        headers=headers)
    res = json.loads(response.content)
    token = res['access_token']
    return token

def getCharacterEquiptment(realmSlug, characterName):
    token = getToken()
    headers = {
        'Authorization' : f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Battlenet-Namespace': 'profile-us',
        'locale': 'en_US'
    }
    response = requests.get(f'{base_url}/profile/wow/character/{realmSlug}/{characterName}/equipment', headers=headers)
    return json.loads(response.content)

def getCharacterMounts(realmSlug, characterName):
    token = getToken()
    headers = {
        'Authorization' : f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Battlenet-Namespace': 'profile-us',
        'locale': 'en_US'
    }
    response = requests.get(f'{base_url}/profile/wow/character/{realmSlug}/{characterName}/collections/mounts', headers=headers)
    return json.loads(response.content)

def prettyPrint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

def dumpToFile(obj):
    with open('info.json', 'w') as f:
        json.dump(obj, f, indent=4, sort_keys=True)

dumpToFile(getCharacterMounts('turalyon', 'yurasaki'))