import json
import os
import glob

json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
# output_csv_file_path = os.path.join("C:", os.sep, "output", "edit", "info", "20mins_or_less.csv")
output_csv_file_path = os.path.join("C:", os.sep, "output", "edit", "info", "more_then_20mins.csv")

# しばらく決め打ち
SMITE_SPELL_ID = 11
SOLO_DUO_Q = 420
TWENTY_MINUTE_SECONDS = 1200

with open(output_csv_file_path, 'w') as csv_f:

    tmp = ""
    for i in range(5):
        tmp += ",championId{0},role{0},lane{0},haveSmite{0}".format(i)

    # 項目名の出力
    csv_f.write(tmp[1:])
    csv_f.write("\n")

    # 1試合づつ読み込み
    for json_file_path in json_files_path:
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)

            # ランク戦のみ取り込んでいるはずが、チュートリアルのデータも入ってる
            # 不要なので、読み飛ばす
            if json_data['queueId'] != SOLO_DUO_Q:
                # print("{0} is skipped".format(game_id))
                continue

            # 試合時間20分以下のデータは扱わない
            if json_data['gameDuration'] <= TWENTY_MINUTE_SECONDS:

            # 試合時間20分超のデータは扱わない
            # if json_data['gameDuration'] > TWENTY_MINUTE_SECONDS:
                continue

            print(game_id, json_data['gameDuration'])

            participants = json_data['participants']

            participants_of_match = {}
            cnt = 0

            for participant in participants:
                # print(participant["participantId"])
                # tmp_participant = OrderedDict()

                tmp_participant = {}

                tmp_participant['participantId'] = participant["participantId"]
                tmp_participant['championId'] = participant["championId"]
                tmp_participant['role'] = participant["timeline"]["role"]
                tmp_participant['lane'] = participant["timeline"]["lane"]

                if participant["spell1Id"] == SMITE_SPELL_ID or participant["spell2Id"] == SMITE_SPELL_ID:
                    tmp_participant["smite"] = 1

                else:
                    tmp_participant["smite"] = 0

                participants_of_match[participant["participantId"]] = tmp_participant

            tmp = ""
            for i in range(0, 2):
                # print(i)

                # 1-5, 6-10と1チーム5人ずつ設定し、出力する
                for x in range(i * 5 + 1, i * 5 + 6):
                    tmp += ',{championId},{role},{lane},{smite},{support_item}'.format(championId=participants_of_match[x]["championId"],
                                                                          role=participants_of_match[x]["role"],
                                                                          lane=participants_of_match[x]["lane"],
                                                                          smite=participants_of_match[x]["smite"])
                # 異常ケースを含むチームがあるかどうかのざっくり目視確認
                # print(tmp)

                csv_f.write(tmp[1:])
                csv_f.write("\n")
                tmp = ""

print("ended")
