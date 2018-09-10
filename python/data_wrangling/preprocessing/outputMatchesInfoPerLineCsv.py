import json
import os
import glob

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

# # array(['NONE', 'SOLO', 'DUO_CARRY', 'DUO_SUPPORT', 'DUO'], dtype=object)


def convert_role_to_num(role):
    if role == "NONE":
        return 1

    elif role == "SOLO":
        return 2

    elif role == "DUO":
        return 3

    elif role == "DUO_CARRY":
        return 4

    elif role == "DUO_SUPPORT":
        return 5

    else:
        return 99


def convert_lane_to_num(lane):
    if lane == "TOP":
        return 1

    elif lane == "JUNGLE":
        return 2

    elif lane == "MIDDLE":
        return 3

    elif lane == "BOTTOM":
        return 4

    else:
        return 99


def adjust_participantId(participantId):
    if participantId < 6:
        return participantId

    else:
        return participantId - 5

with open(output_csv_file_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("gameId,participantId,championId,role,lane,haveSmite\n")

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

                # 試合時間20分超のデータは扱わない
                # if json_data['gameDuration'] > TWENTY_MINUTE_SECONDS:
                continue

            participants = json_data['participants']

            # print(participants)

            participants_of_match = {}
            cnt = 0

            for participant in participants:
                tmp_participant = {}
                tmp_participant['participantId'] = adjust_participantId(participant["participantId"])
                tmp_participant['championId'] = participant["championId"]

                # array(['NONE', 'SOLO', 'DUO_CARRY', 'DUO_SUPPORT', 'DUO'], dtype=object)
                # tmp_participant['role'] = convert_role_to_num(participant["timeline"]["role"])
                tmp_participant['role'] = participant["timeline"]["role"]

                # array(['JUNGLE', 'TOP', 'MIDDLE', 'BOTTOM'], dtype=object)
                # tmp_participant['lane'] = convert_lane_to_num(participant["timeline"]["lane"])
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

print("ended")