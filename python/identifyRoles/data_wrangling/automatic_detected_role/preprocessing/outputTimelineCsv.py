import json
import os
import glob

# /lol/match/v3/timelines/by-match/{matchId}から出力されたJSONから
# ゲームID, 参加者ID, サポートアイテム持ちフラグを取得し、csvファイルに出力する
# サポートアイテム持ちフラグ 0:サポートアイテム不所持　1:サポートアイテム所持
json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "timeline", "*.json"))
output_csv_file_path = os.path.join("C:", os.sep, "output", "edit", "timeline", "HadSupportItem.csv")

# これらのいずれかに該当したら、サポートアイテム所持の扱い
# NOMADS_MEDALLION_ID = 3096
# TARGONS_BRACE_ID = 3097
# FROSTFANG_ID = 3098
SUPPORT_ITEM_IDS = [3096, 3097, 3098]

with open(output_csv_file_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("gameId,participantId,haveSupportItem\n")

    total_file_num = len(json_files_path)
    cnt = 0

    # 1試合づつ読み込み
    for json_file_path in json_files_path:
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)

            tmp = [0 for i in range(10)]

            for frame in json_data['frames']:
                if not frame['events']:
                    continue

                for event in frame['events']:
                    # print(event)

                    if event['type'] != "ITEM_PURCHASED":
                        continue

                    if event['itemId'] in SUPPORT_ITEM_IDS:
                        # participantIdは1から始まるので、0から始まるように調整
                        tmp[event['participantId'] - 1] = 1

            for index, have_support_item in enumerate(tmp):
                # print(i)

                tmp_str = '{gameId},{participantId},{haveSupportItem}\n'.format(gameId=game_id,
                                                                                participantId=index + 1,
                                                                                haveSupportItem=have_support_item)

                csv_f.write(tmp_str)
                tmp = ""
        cnt += 1
        
        if cnt % 100 == 0:
            print("{0}/{1}".format(cnt, total_file_num))

print("ended")
