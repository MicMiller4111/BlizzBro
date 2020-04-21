import requests
from requests.auth import HTTPBasicAuth
import json
from src.blizzardapis.wow_apis import WowApi



def prettyPrint(obj):
    print(json.dumps(obj, indent=4, sort_keys=True))

def dumpToFile(obj):
    with open('info.json', 'w') as f:
        json.dump(obj, f, indent=4, sort_keys=True)

character = WowApi.getCharacter('turalyon', 'yurasaki')

print(character['equipped_item_level'])
