import json
import os
import glob

import edit_values as ev

# /lol/match/v3/matches/{matchId}から出力されたJSONから
# ゲームID, 参加者ID, チャンピオンID, ロール, レーン, スマイト持ちフラグを取得し、csvファイルに出力する
json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
output_csv_file_path = os.path.join("C:", os.sep, "output", "edit", "info", "info_per_line.csv")

i = 1
json_docs = []

# しばらく決め打ち
SMITE_SPELL_ID = 11
SOLO_DUO_Q = 420
TWENTY_MINUTE_SECONDS = 1200
with open(output_csv_file_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("gameId,participantId,championId,role,lane,haveSmite\n")

    total_file_num = len(json_files_path)
    cnt = 0

    for json_file_path in json_files_path:
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        # print(game_id)

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)

            # ランク戦のみ取っているはずなのに、チュートリアルのデータも入ってる
            # 不要なので、読み飛ばす
            if json_data['queueId'] != SOLO_DUO_Q:
            #    print("{0} is skipped".format(game_id))
                continue

            # 試合時間20分以下のデータは扱わない
            if json_data['gameDuration'] <= TWENTY_MINUTE_SECONDS:
                continue

            participants = json_data['participants']
            participants_of_match = {}

            for participant in participants:
                tmp_participant = {}
                # tmp_participant['participantId'] = ev.adjust_participantId(participant["participantId"])
                tmp_participant['participantId'] = participant["participantId"]
                tmp_participant['championId'] = participant["championId"]

                # array(['NONE', 'SOLO', 'DUO_CARRY', 'DUO_SUPPORT', 'DUO'], dtype=object)
                # tmp_participant['role'] = ev.convert_role_to_num(participant["timeline"]["role"])
                tmp_participant['role'] = participant["timeline"]["role"]

                # array(['JUNGLE', 'TOP', 'MIDDLE', 'BOTTOM'], dtype=object)
                # tmp_participant['lane'] = ev.convert_lane_to_num(participant["timeline"]["lane"])
                tmp_participant['lane'] = participant["timeline"]["lane"]

                if participant["spell1Id"] == SMITE_SPELL_ID or participant["spell2Id"] == SMITE_SPELL_ID:
                    tmp_participant["smite"] = 1

                else:
                    tmp_participant["smite"] = 0

                participants_of_match[participant["participantId"]] = tmp_participant

            for i in range(1, 11):
                tmp = '{gameId},{participantId},{championId},{role},{lane},{smite}\n'.format(
                    gameId=game_id,
                    participantId=participants_of_match[i]["participantId"],
                    championId=participants_of_match[i]["championId"],
                    role=participants_of_match[i]["role"],
                    lane=participants_of_match[i]["lane"],
                    smite=participants_of_match[i]["smite"])

                # print(tmp)

                csv_f.write(tmp)

        cnt += 1

        if cnt % 100 == 0:
            print("{0}/{1}".format(cnt, total_file_num))
print("ended")