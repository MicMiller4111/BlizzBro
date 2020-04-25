# Do this to auth the app
# client_id = client_id_here
# auth_url = 'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'.format(client_id)
# open url above in chrome/firefox

import discord
import json
from src.blizzardapis.wow_apis import WowApi
from src.common.message_formatter import MessageFormatter

with open("config.json") as config:
    config = json.load(config)

with open("help.json") as help_config:
    help_config = json.load(help_config)

TOKEN = config["token"]

mounts = WowApi.get_all_mounts()

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

        if message.content.startswith("!wow-character"):
            user_input = message.content.split(" ")
            server = user_input[1]
            character = user_input[2]
            info = WowApi.character(server.lower(), character.lower())
            char_media = WowApi.render_character(server.lower(), character.lower())
            render = char_media["render_url"]
            custom_message = MessageFormatter.build_character_info(info)
            custom_message += f"\r{render}"
            await self.send_message(message, custom_message)
        
        if message.content.startswith("!wow-gear"):
            user_input = message.content.split(" ")
            server = user_input[1]
            character = user_input[2]
            info = WowApi.character_equiptment(server.lower(), character.lower())
            custom_message = MessageFormatter.build_equiptment(info)
            await self.send_message(message, custom_message)
        
        if message.content.startswith("!wow-character-mounts"):
            user_input = message.content.split(" ")
            server = user_input[1]
            character = user_input[2]
            info = WowApi.character_mounts(server.lower(), character.lower())
            custom_message = MessageFormatter.build_character_mounts(info)
            for i in custom_message:
                await self.send_message(message, i)
        
        if message.content.startswith("!wow-mount"):
            user_input = message.content.split(" ")
            mount = ""
            for i in user_input:
                if(i != user_input[0]):
                    mount += f"{i} "
            info = WowApi.mount(mounts[mount.rstrip()])
            custom_message = MessageFormatter.build_mount(info)
            await self.send_message(message, custom_message)

        if message.content == "!help":
            print(message.content)
            custom_message = MessageFormatter.help_info(help_config)
            await self.send_message(message, custom_message)
        return

    async def send_message(self, message, custom_message):
        await message.channel.send(custom_message)
        return

client = MyClient()
client.run(TOKEN)