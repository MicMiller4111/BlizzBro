import json

class MessageFormatter:
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
    
    async def help_info(self, help_config):
        custom_message = "Functions"
        for com in help_config:
            desctiption = help_config[com]["description"]
            example = help_config[com]["example"]
            custom_message += f"\nCommand: {com}\tExample: {example}\tDescription: {desctiption}"
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