import json
import os
import glob

# /lol/match/v3/timelines/by-match/{matchId}から出力されたJSONから
# ゲームID, チームID、勝利フラグをcsvファイル形式で出力する
json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
win_team_log_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "win_team_log.csv")

TWENTY_MINUTE_SECONDS = 1200

with open(win_team_log_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("game_id,team_id,win_flag,total_time\n")

    total_file_num = len(json_files_path)

    # 1試合づつ読み込み
    for file_index, json_file_path in enumerate(json_files_path):
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)

            total_time = json_data['gameDuration']

            # 試合時間20分以下のデータは扱わない
            if total_time <= TWENTY_MINUTE_SECONDS:
                continue

            for team in json_data['teams']:
                if team['win'] == "Win":
                    win_flag = 1
                else:
                    win_flag = 0

                tmp_str = '{game_id},{team_id},{win_flag},{total_time}\n' .format(game_id=game_id, \
                                                                                  team_id=team["teamId"], \
                                                                                  win_flag=win_flag, \
                                                                                  total_time=total_time)
                csv_f.write(tmp_str)

        if file_index % 100 == 0:
            print("{0}/{1}".format(file_index, total_file_num))

print("ended")