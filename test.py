# Do this to auth the app
# client_id = client_id_here
# auth_url = 'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'.format(client_id)
# open url above in chrome/firefox

import discord
import json
from src.blizzardapis.wow_apis import WowApi

with open("config.json") as config:
    config = json.load(config)

TOKEN = config['token']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
            print(message.content)

        if message.content.startswith('!wow-char'):
            user_input = message.content.split(' ')
            server = user_input[1]
            character = user_input[2]
            info = WowApi.getCharacter(server.lower(), character.lower())
            custom_message = await self.build_character_info(info)
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
client = MyClient()
client.run(TOKEN)