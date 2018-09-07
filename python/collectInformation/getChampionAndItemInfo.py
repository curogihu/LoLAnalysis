import utility
import json

import codecs

champions_json = utility.get_lol_game_champion_info_json()
items_json = utility.get_lol_item_info_json()

if champions_json:
    with codecs.open(utility.champions_file_path, 'w', 'utf-8') as f_champions:
        try:
            json.dump(champions_json["data"], f_champions, ensure_ascii=False, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getChampionInfo]")

if items_json:
    with codecs.open(utility.items_file_path, 'w', 'utf-8') as f_items:
        try:
            json.dump(items_json["data"], f_items, ensure_ascii=False, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getChampionInfo]")
