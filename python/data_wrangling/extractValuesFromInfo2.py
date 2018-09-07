import json
import os
import glob

# /lol/match/v3/matches/{matchId}から出力されたJSONから
# ゲームID, 参加者ID, チャンピオンID, ロール, レーン, スマイト持ちフラグを取得し、csvファイルに出力する
json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
output_csv_file_path = glob.glob(os.path.join("C:", os.sep, "output", "edit", "info", "edit.csv"))

i = 1
json_docs = []

# しばらく決め打ち
SMITE_SPELL_ID = 11
SOLO_DUO_Q = 420

with open('C:\output\edit\info\output2.csv', 'w') as csv_f:

    # 項目名の出力
    csv_f.write("gameId,participantId,championId,role,lane,haveSmite\n")

    for json_file_path in json_files_path:
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        print(game_id)

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)

            # ランク戦のみ取っているはずなのに、チュートリアルのデータも入ってる
            # 不要なので、読み飛ばす
            if json_data['queueId'] != SOLO_DUO_Q:
                print("{0} is skipped".format(game_id))
                continue

            participants = json_data['participants']

            # print(participants)

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
                # 1-5, 6-10と1チーム5人ずつ出力
                for x in range(i * 5 + 1, i * 5 + 6):
                    tmp = '{gameId},{participantId},{championId},{role},{lane},{smite}\n'.format(
                                                                            gameId=game_id,
                                                                            participantId=participants_of_match[x]["participantId"],
                                                                            championId=participants_of_match[x]["championId"],
                                                                            role=participants_of_match[x]["role"],
                                                                            lane=participants_of_match[x]["lane"],
                                                                            smite=participants_of_match[x]["smite"])

                    csv_f.write(tmp)
                    tmp = ""

print("ended")
