import json
import os
import glob

# /lol/match/v3/timelines/by-match/{matchId}から出力されたJSONから
# ゲームID, 倒した中立モンスターの種類、倒した数をcsvファイル形式で出力する
json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "timeline", "*.json"))
boss_level_monster_kill_log_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "killed_log.csv")


def convert_to_seconds(target_time):
    return int(target_time / 1000)

with open(boss_level_monster_kill_log_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("game_id,boss_type,team_id,time,amount\n")

    total_file_num = len(json_files_path)
    cnt = 0

    # 1試合づつ読み込み
    for json_file_path in json_files_path:
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
                    else:
                        boss_type = event['monsterType']

                    if 1 <= event['killerId'] <= 5:
                        killer_team = 0

                    else:
                        killer_team = 1

                    if not(boss_type in boss_kill_logs):
                        boss_kill_logs[boss_type] = {0: [], 1: []}

                    boss_kill_logs[boss_type][killer_team].append(event['timestamp'])

            # print(boss_kill_logs)

            # exit()

            for boss_type, teams_logs in boss_kill_logs.items():
                for team_id, team_logs in teams_logs.items():
                    for index, elapsed_time in enumerate(team_logs):
                        tmp_str = '{game_id},{boss_type},{killer_team},{time},{amount}\n' .format(game_id = game_id, \
                                                                                                  boss_type = boss_type, \
                                                                                                  killer_team = team_id, \
                                                                                                  time = convert_to_seconds(elapsed_time), \
                                                                                                  amount = index + 1)

                        csv_f.write(tmp_str)
                        tmp_str = ""
                        cnt += 1

        if cnt % 100 == 0:
            print("{0}/{1}".format(cnt, total_file_num))

print("ended")
