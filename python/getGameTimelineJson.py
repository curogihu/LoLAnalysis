import utility
import json
from datetime import datetime

with open(utility.gameids_file_path) as f_game_ids:
    game_ids = f_game_ids.readlines()

cnt = 0
game_ids_len = len(game_ids)

for game_id in game_ids:
    game_id = game_id.replace("\n", "")

    print("expected game_id json = " + game_id)
    game_info_json = utility.get_lol_game_info_json(utility.game_info_url, str(game_id))

    if game_info_json == "" or game_info_json == "429":
        print("skipped summonerId json = " + game_id)
        continue

    cnt += 1

    if cnt % 10 == 0:
        print(str(cnt) + " / " + str(game_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    print(utility.game_info_directory_path + game_id + ".json")

    with open(utility.game_info_directory_path + game_id + ".json", "w") as f_json:
        try:
            json.dump(game_info_json, f_json, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getMatchjson] game_id = " + game_id)
            # give up getting json
