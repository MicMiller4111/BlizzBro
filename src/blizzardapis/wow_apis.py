import requests
from requests.auth import HTTPBasicAuth
import json
from ..common.oauth import Oauth

base_url = 'https://us.api.blizzard.com'

class WowApi:
    def getCharacterEquiptment(realmSlug, characterName):
        token = Oauth.getToken()
        headers = {
            'Authorization' : f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Battlenet-Namespace': 'profile-us',
            'locale': 'en_US'
        }
        response = requests.get(f'{base_url}/profile/wow/character/{realmSlug}/{characterName}/equipment', headers=headers)
        payload = json.loads(response.content)
        return payload

    def getCharacterMounts(realmSlug, characterName):
        token = Oauth.getToken()
        headers = {
            'Authorization' : f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Battlenet-Namespace': 'profile-us',
            'locale': 'en_US'
        }
        response = requests.get(f'{base_url}/profile/wow/character/{realmSlug}/{characterName}/collections/mounts', headers=headers)
        payload = json.loads(response.content)
        return payload

    def getCharacter(realmSlug, characterName):
        token = Oauth.getToken()
        headers = {
            'Authorization' : f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Battlenet-Namespace': 'profile-us',
            'locale': 'en_US'
        }
        response = requests.get(f'{base_url}/profile/wow/character/{realmSlug}/{characterName}', headers=headers)
        payload = json.loads(response.content)
        return payload
