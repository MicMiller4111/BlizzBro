import requests
from requests.auth import HTTPBasicAuth
import json
from ..common.oauth import Oauth

base_url = 'https://us.api.blizzard.com'

class WowApi:
    def character_equiptment(realmSlug, characterName):
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

    def character_mounts(realmSlug, characterName):
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

    def character(realmSlug, characterName):
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

    def render_character(realmSlug, characterName):
        token = Oauth.getToken()
        headers = {
            'Authorization' : f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Battlenet-Namespace': 'profile-us',
            'locale': 'en_US'
        }
        response = requests.get(f'{base_url}/profile/wow/character/{realmSlug}/{characterName}/character-media', headers=headers)
        payload = json.loads(response.content)
        return payload
    
    def get_all_mounts():
        token = Oauth.getToken()
        headers = {
            'Authorization' : f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Battlenet-Namespace': 'static-us',
            'locale': 'en_US'
        }
        response = requests.get(f'{base_url}/data/wow/mount/index', headers=headers)
        payload = json.loads(response.content)
        mounts = {}
        for mount in payload["mounts"]:
            mounts[mount["name"]["en_US"]] = mount["id"]
        return mounts
    
    def get_mount_pic_api(mountId):
        token = Oauth.getToken()
        headers = {
            'Authorization' : f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Battlenet-Namespace': 'static-us',
            'locale': 'en_US'
        }
        response = requests.get(f'{base_url}/data/wow/mount/{mountId}', headers=headers)
        payload = json.loads(response.content)
        return payload["creature_displays"][0]["key"]["href"]
    
    def mount(mountId):
        extractedUrl = WowApi.get_mount_pic_api(mountId)
        token = Oauth.getToken()
        headers = {
            'Authorization' : f'Bearer {token}',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Battlenet-Namespace': 'static-us',
            'locale': 'en_US'
        }
        response = requests.get(extractedUrl, headers=headers)
        payload = json.loads(response.content)
        return payload