import json
import os
import numpy as np
from glob import glob

BLUE = 0
RED = 1


def convert_team_color_id(participant_id: int) -> int:
    if 1 <= participant_id <= 5:
        return BLUE

    else:
        return RED


def extract_participant_info(info_path, _json, target_player_name):
    game_id = os.path.splitext(os.path.basename(info_path))[0]
    participantIdentities = _json['participantIdentities']

    # print(participantIdentities)

    for participantIdentity in participantIdentities:
        if participantIdentity['player']['summonerName'] == target_player_name:
            participant_id = participantIdentity['participantId']
            team_id = convert_team_color_id(participant_id)
            # print(game_id, participant_id, team_id)

            result = _json['teams'][team_id]['win']

            return game_id, participant_id, team_id, result

    return None, None, None, None


def extract_game_duration(_json):
    print(_json['gameDuration'], _json['gameDuration'] // 60, _json['gameDuration'] % 60)
    return _json['gameDuration'], _json['gameDuration'] // 60, _json['gameDuration'] % 60


format_path = 'C:/output/game/garen/info/*.json'
target_player_name = 'でかびたん'
# print(sorted(glob(paths)))

info_paths = sorted(glob(format_path))

# tmp_path = info_paths[0]

infos = []

for info_path in info_paths:
    json_open = open(info_path, 'r')
    json_info = json.load(json_open)
    game_id, pariticipant_id, team_id, result = extract_participant_info(info_path, json_info, target_player_name)
    game_duration, game_minutes, game_seconds = extract_game_duration(json_info)

    infos.append([game_id, pariticipant_id, team_id, result, game_duration, game_minutes, game_seconds])
    # infos.append([game_id, pariticipant_id, team_id, result])


# print(np.array(infos))
infos_np = np.array(infos)



    