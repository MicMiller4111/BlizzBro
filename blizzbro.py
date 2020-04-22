# Do this to auth the app
# client_id = client_id_here
# auth_url = 'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'.format(client_id)
# open url above in chrome/firefox

import discord
import json
from src.blizzardapis.wow_apis import WowApi

with open("config.json") as config:
    config = json.load(config)

with open("help.json") as help_config:
    help_config = json.load(help_config)

TOKEN = config["token"]

class MyClient(discord.Client):    
    async def on_ready(self):
        print("Logged on as", self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong")
            print(message.content)

        if message.content.startswith("!wow-char"):
            user_input = message.content.split(" ")
            server = user_input[1]
            character = user_input[2]
            info = WowApi.character(server.lower(), character.lower())
            custom_message = await self.build_character_info(info)
            await self.send_message(message, custom_message)
        
        if message.content.startswith("!wow-gear"):
            user_input = message.content.split(" ")
            server = user_input[1]
            character = user_input[2]
            info = WowApi.character_equiptment(server.lower(), character.lower())
            custom_message = await self.build_equiptment(info)
            await self.send_message(message, custom_message)
        
        if message.content.startswith("!wow-mounts"):
            user_input = message.content.split(" ")
            server = user_input[1]
            character = user_input[2]
            info = WowApi.character_mounts(server.lower(), character.lower())
            custom_message = await self.build_mounts(info)
            await self.send_message(message, custom_message)

        if message.content == "!help":
            print(message.content)
            custom_message = "Functions"
            for com in help_config:
                desctiption = help_config[com]["description"]
                example = help_config[com]["example"]
                custom_message += f"\nCommand: {com}\tExample: {example}\tDescription: {desctiption}"
            await self.send_message(message, custom_message)
        return

    async def send_message(self, message, custom_message):
        await message.channel.send(custom_message)
        return
    
    async def build_character_info(self, info):
        faction = info["faction"]["name"]["en_US"]
        guild = info["guild"]["name"]
        title = info["active_title"]["name"]["en_US"]
        hero_class = info["character_class"]["name"]["en_US"]
        ilvl = info["equipped_item_level"]
        custom_message = f"Faction: {faction}"
        custom_message += f"\nGuild: {guild}"
        custom_message += f"\nTitle: {title}"
        custom_message += f"\nClass: {hero_class}"
        custom_message += f"\nEquipped Ilvl = {ilvl}"
        return custom_message
    
    async def help_info(self):
        custom_message = ""
        for com in help_config:
            desctiption = help_config[com]["description"]
            example = help_config[com]["example"]
            custom_message += f"Command: {com}\tEx.: {example}\tDescription: {desctiption}\n"
        return custom_message
    
    async def build_equiptment(self, info):
        length = len(info["equipped_items"])
        i = 0
        custom_message = "Items\r"
        while i < length:
            item_slot = info["equipped_items"][i]["slot"]["name"]["en_US"]
            item_quality = info["equipped_items"][i]["quality"]["name"]["en_US"] 
            item_ilvl = info["equipped_items"][i]["level"]["value"]
            item_name = info["equipped_items"][i]["name"]["en_US"]
            custom_message += f"Slot: {item_slot}, Name: {item_name}, Quality: {item_quality}, Ilvl: {item_ilvl}\n"
            i += 1
        return custom_message

    async def build_mounts(self, info):
        length = len(info["mounts"])
        i = 0
        custom_message = "Mounts\r"
        while i < length:
            mount = info["mounts"][i]["mount"]["name"]["en_US"]
            if(i == length - 1):
                custom_message += f"{mount}"
            else:
                custom_message += f"{mount}, "
            i += 1
        return custom_message

client = MyClient()
client.run(TOKEN)