import utility
import json

champions_json = utility.get_lol_game_champion_info_json()
items_json = utility.get_lol_item_info_json()

if champions_json:
    with open(utility.champions_file_path, 'w') as f_champions:
        try:
            json.dump(champions_json["data"], f_champions, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getChampionInfo]")

if items_json:
    with open(utility.items_file_path, 'w') as f_items:
        try:
            json.dump(items_json["data"], f_items, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getChampionInfo]")
