import json
from src.blizzardapis.wow_apis import WowApi

#with open("info.json", "w") as f:
#    f.write(json.dumps(WowApi.character_mounts('turalyon', 'yurasaki'), indent=4, sort_keys=True))

mounts = WowApi.character_mounts('turalyon', 'yurasaki')


length = len(mounts["mounts"])
i = 0
custom_message = "Mounts\r"
while i < length:
    mount = mounts["mounts"][i]["mount"]["name"]["en_US"]
    if(i == length - 1):
        custom_message += f"{mount}"
    else:
        custom_message += f"{mount}, "
    i += 1
print(custom_message)