import json
import os
import sys
import glob
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

sys.path.append('../collectInformation')
import utility

print("start", datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'timeout': 60}])
info_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
timeline_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "timeline", "*.json"))
es = Elasticsearch(['http://127.0.0.1:9200/'])

def extract_match_info_from_json(p_info_files_path):
    dict_account_id = utility.get_dict_account_id()

    for info_file_path in p_info_files_path:
        game_id, ext = os.path.splitext(os.path.basename(info_file_path))

        with open(info_file_path, 'r') as f:
            info_json = json.load(f)

            team_json = info_json["teams"]
            team_dict = {}

            for team in team_json:
                if team["win"] == "Win":
                    team_dict[team["teamId"]] = 1

                else: #  in case of "Fail"
                    team_dict[team["teamId"]] = 0

            for participant_identity in info_json["participantIdentities"]:
                current_account_id = participant_identity["player"]["currentAccountId"]

                if current_account_id in dict_account_id:
                    participant_dict = {}
                    participant_dict["participantId"] = participant_identity["participantId"]
                    participant_dict["gameId"] = game_id
                    # dict_timeline[game_id][current_account_id]["accountId"] = current_account_id
                    dict_timeline[game_id + "_" + str(participant_identity["participantId"])] = participant_dict

            for participant in info_json["participants"]:
                dict_key = game_id + "_" + str(participant["participantId"])

                if dict_key in dict_timeline:
                    dict_timeline[dict_key]["win"] = team_dict[participant["teamId"]]
                    dict_timeline[dict_key]["teamId"] = participant["teamId"]
                    dict_timeline[dict_key]["championId"] = participant["championId"]
                    dict_timeline[dict_key]["role"] = participant["timeline"]["role"]
                    dict_timeline[dict_key]["lane"] = participant["timeline"]["lane"]

    return dict_timeline

dict_timeline = {}
dict_timeline = extract_match_info_from_json(info_files_path)

print("finished extracting match information from json", datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

es_index = 1
actions = []

for timeline_file_path in timeline_files_path:
    game_id, ext = os.path.splitext(os.path.basename(timeline_file_path))

    with open(timeline_file_path, 'r') as f:
        timeline_json = json.load(f)

        for frame in timeline_json['frames']:

            if frame['events']:
                timeline_list = {}
                for event in frame['events']:
                    if event['type'] == 'ITEM_PURCHASED' and \
                                                    str(game_id) + "_" + str(event["participantId"]) in dict_timeline:

                        dict_key = str(game_id) + "_" + str(event["participantId"])

                        output_dict = {}
                        output_dict["gameId"] = game_id
                        output_dict["participantId"] = str(event["participantId"])
                        output_dict["championId"] = dict_timeline[dict_key]["championId"]
                        output_dict["role"] = dict_timeline[dict_key]["role"]
                        output_dict["lane"] = dict_timeline[dict_key]["lane"]
                        output_dict["win"] = dict_timeline[dict_key]["win"]
                        output_dict["itemId"] = event['itemId']
                        output_dict["timestamp"] = event['timestamp']

                        actions.append({'_index':'timelines', '_type':'timeline', '_source':output_dict})

                        if len(actions) > 1000:
                            helpers.bulk(es, actions)
                            print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                            actions = []

if len(actions) > 0:
    helpers.bulk(es, actions)

print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))


"""
for timeline_file_path in timeline_files_path:
    game_id, ext = os.path.splitext(os.path.basename(timeline_file_path))

    with open(timeline_file_path, 'r') as f:
        timeline_json = json.load(f)

        for frame in timeline_json['frames']:

            if frame['events']:
                timeline_list = {}
                for event in frame['events']:
                    if event['type'] == 'ITEM_PURCHASED' and \
                            str(game_id) + "_" + str(event["participantId"]) in dict_timeline:

                        dict_key = str(game_id) + "_" + str(event["participantId"])

                        output_dict = {}
                        output_dict["championId"] = dict_timeline[dict_key]["championId"]
                        output_dict["role"] = dict_timeline[dict_key]["role"]
                        output_dict["lane"] = dict_timeline[dict_key]["lane"]
                        output_dict["win"] = dict_timeline[dict_key]["win"]
                        output_dict["itemId"] = event['itemId']
                        output_dict["timestamp"] = event['timestamp']

                        print(es_index, d   atetime.now().strftime("%Y/%m/%d %H:%M:%S"))

                        es.index(index='timelines', doc_type='timeline', id=es_index, body=output_dict)
                        es_index += 1
"""


print(datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

print("ended")