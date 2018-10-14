
"""
match

participantIdentitiesを取得
participantsからparticipantId, teamId, championId, stats["win"]を取得


[current_account_id]


region_id, game_id, account_id, champion_id, win_flag


region_id, region_str


champion_id, region_id, champion_key, champion_name



"""

import json
import os
import glob

# /lol/match/v3/timelines/by-match/{matchId}から出力されたJSONから
# ゲームID, 倒した中立モンスターの種類、倒した数をcsvファイル形式で出力する
if os.name == " nt":
    json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
    output_log_path = os.path.join("C:", os.sep, "output", "edit", "find_natural_enemies", "log.csv")

elif os.name == "posix":
    json_files_path = glob.glob(os.path.join('', os.sep, 'Applications', 'output', 'game', 'info', '*.json'))
    output_log_path = os.path.join('', os.sep, "Applications", "output", "edit", "find_natural_enemies", "log.csv")


with open(output_log_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("region_id,game_id,account_id,champion_id,team_id,win_flag\n")
    total_file_num = len(json_files_path)

    # 1試合づつ読み込み
    for file_index, json_file_path in enumerate(json_files_path):
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)

            # boss_kill_logs = {}

            participants = {}

            for participant_identity in json_data['participantIdentities']:
                # print(participant_identity["participantId"])
                # print(participant_identity["player"]["currentAccountId"])

                participants[participant_identity["participantId"]] = {"accountId": participant_identity["player"]["currentAccountId"]}

            for participant in json_data["participants"]:
                participants[participant["participantId"]]["championId"] = participant["championId"]
                participants[participant["participantId"]]["winFlag"] = participant["stats"]["win"]

            for data in participants.values():
                # print(data)
                # print(data["accountId"])
                # print(data["championId"])
                # print(data["winFlag"])

                tmp_str = '{region_id},{game_id},{account_id},{champion_id},{win_flag}\n' \
                                .format(region_id="jp",
                                        game_id=game_id, \
                                        account_id=data['accountId'], \
                                        champion_id=data['championId'], \
                                        win_flag=data['winFlag'] + 0)
                csv_f.write(tmp_str)

        if file_index % 100 == 0:
            print("{0}/{1}".format(file_index, total_file_num))

print("ended")
