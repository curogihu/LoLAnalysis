import json
import os
import glob
from collections import OrderedDict

import csv

json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
output_csv_file_path = glob.glob(os.path.join("C:", os.sep, "output", "edit", "info", "edit.csv"))

i = 1
json_docs = []

# しばらく決め打ち
SMITE_SPELL_ID = 11

with open('output.csv', 'w') as csv_f:
    # writer = csv.writer(csv_f, lineterminator='\n')

    tmp = ""
    for i in range(5):
        tmp += ",championId{0},role{0},lane{0},haveSmite{0},haveSupportItem{0}".format(i)

    # 項目名の出力
    csv_f.write(tmp[1:])
    csv_f.write("\n")

    for json_file_path in json_files_path:
        game_id, ext = os.path.splitext(os.path.basename(json_file_path))

        print(game_id)

        with open(json_file_path, 'r') as f:
            json_data = json.load(f)
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

            # print(participants_of_match)

            # print(participants_of_match)

            # print(str(participants_of_match[1]["championId"] + "," + tmp_participant[1]['role'] + "," + tmp_participant['lane'] + "," + tmp_participant['smite'])

            """
            print('{championId},{role},{lane},{smite}'.format(championId=participants_of_match[1]["championId"],
                                                              role=participants_of_match[1]["role"],
                                                              lane=participants_of_match[1]["lane"],
                                                              smite=participants_of_match[1]["smite"]))
            """
            tmp = ""

            for i in range(0, 2):
                # print(i)

                for x in range(i * 5 + 1, i * 5 + 6):
                    tmp += ',{championId},{role},{lane},{smite},{support_item}'.format(championId=participants_of_match[x]["championId"],
                                                                          role=participants_of_match[x]["role"],
                                                                          lane=participants_of_match[x]["lane"],
                                                                          smite=participants_of_match[x]["smite"],
                                                                            support_item="")

                # print(tmp)

                csv_f.write(tmp[1:])
                csv_f.write("\n")
                tmp = ""

print("ended")
