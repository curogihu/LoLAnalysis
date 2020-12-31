"https://jp1.api.riotgames.com/lol/static-data/v3/items?locale=ja_JP&api_key=[APIKEY]"

import utility

items_json = utility.get_lol_item_info_json()

if items_json:
    with open(utility.items_file_path, 'w', encoding="UTF-8") as f_items:
        item_data = items_json["data"]

        for item_info in item_data.values():
            print(item_info)

            # print(item_info)
            f_items.write(str(item_info["id"]) + "\n")
             #                         item_info["name"] + "\n")
       #                       item_info["description"] + "\n")
