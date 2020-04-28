import json

class MessageFormatter:
    def build_character_info(info):
        custom_message = "Character\r"
        faction = info["faction"]["name"]["en_US"]
        custom_message += f"Faction: {faction}"
        if(info.get("guild", False) != False):
            guild = info["guild"]["name"]
            custom_message += f"\nGuild: {guild}"
        if(info.get("active_title", False) != False):
            title = info["active_title"]["name"]["en_US"]
            custom_message += f"\nTitle: {title}"
        hero_class = info["character_class"]["name"]["en_US"]
        custom_message += f"\nClass: {hero_class}"
        ilvl = info["equipped_item_level"]
        custom_message += f"\nEquipped Ilvl = {ilvl}"
        return custom_message
    
    def help_info(help_config):
        custom_message = "Functions"
        for com in help_config:
            desctiption = help_config[com]["description"]
            example = help_config[com]["example"]
            custom_message += f"\nCommand: {com}\tExample: {example}\tDescription: {desctiption}"
        return custom_message
    
    def build_equiptment(info):
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

    def build_character_mounts(info):
        length = len(info["mounts"])
        i = 0
        message_array = []
        custom_message = "Mounts\r"
        while i < length:
            mount = info["mounts"][i]["mount"]["name"]["en_US"]
            if(i != length - 1 and len(custom_message + mount) < 2000):
                custom_message += f"{mount}, "
            elif(i != length - 1 and len(custom_message + mount) > 1999):
                message_array.append(custom_message)
                custom_message = ""
                custom_message += f"{mount}, "
            elif(i == length - 1 and len(custom_message + mount) > 1999):
                message_array.append(custom_message)
                custom_message = ""
                custom_message += f"{mount}"
                message_array.append(custom_message)
            else:
                custom_message += f"{mount}"
                message_array.append(custom_message)
            i += 1
        return message_array
    
    def build_mount(info):
        custom_message = info["assets"][0]["value"]
        return custom_message

    def build_realm_status(info):
        status = info["status"]["name"]["en_US"]
        custom_message = f"Server is {status}"
        return custom_message