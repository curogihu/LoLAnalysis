import json
import os
import glob

# /lol/match/v3/timelines/by-match/{matchId}から出力されたJSONから
# ゲームID, 倒した中立モンスターの種類、倒した数をcsvファイル形式で出力する
# json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "timeline", "*.json"))
# boss_level_monster_kill_log_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "killed_log.csv")

json_files_path = glob.glob(os.path.join("", os.sep, "Applications", "output", "game", "timeline", "*.json"))
boss_level_monster_kill_log_path = os.path.join("", os.sep, "Applications", "output", "edit", "boss_killed_log", "killed_log.csv")

def convert_to_seconds(target_time):
    return int(target_time / 1000)


def convert_to_right_team_id(target_id):
    if target_id == 0:
        return 100
    return 200

with open(boss_level_monster_kill_log_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("game_id,boss_type,team_id,time,amount\n")

    total_file_num = len(json_files_path)

    # 1試合づつ読み込み
    for file_index, json_file_path in enumerate(json_files_path):
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)

            boss_kill_logs = {}

            for frame in json_data['frames']:
                if not frame['events']:
                    continue

                for event in frame['events']:
                    # print(event)

                    if event['type'] != "ELITE_MONSTER_KILL":
                        continue

                    if event['monsterType'] == "DRAGON":
                        boss_type = event['monsterSubType']
                        # if event['monsterSubType'] == "FIRE_DRAGON":
                        #    boss_type = event['monsterSubType']
                        # else:
                        #    continue
                    else:
                        boss_type = event['monsterType']
                        # continue

                    if 1 <= event['killerId'] <= 5:
                        killer_team = 0

                    else:
                        killer_team = 1

                    if not(boss_type in boss_kill_logs):
                        boss_kill_logs[boss_type] = {0: [], 1: []}

                    boss_kill_logs[boss_type][killer_team].append(event['timestamp'])

            for boss_type, teams_logs in boss_kill_logs.items():
                for team_id, team_logs in teams_logs.items():
                    for index, elapsed_time in enumerate(team_logs):
                        tmp_str = '{game_id},{boss_type},{killer_team},{time},{amount}\n' .format(game_id=game_id, \
                                                                                                  boss_type=boss_type, \
                                                                                                  killer_team=convert_to_right_team_id(team_id), \
                                                                                                  time=convert_to_seconds(elapsed_time), \
                                                                                                  amount=index + 1)

                        csv_f.write(tmp_str)

        if file_index % 100 == 0:
            print("{0}/{1}".format(file_index, total_file_num))

print("ended")
