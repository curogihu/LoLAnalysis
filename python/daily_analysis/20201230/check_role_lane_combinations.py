import json
import os
import numpy as np

from glob import glob
from tqdm import tqdm


def is_top_role(role: str, lane: str) -> bool:
    if role == 'SOLO' and lane == 'TOP':
        return True

    else:
        return False


def extract_game_id(file_path: str) -> int:
    return int(os.path.splitext(os.path.basename(file_path))[0])


def main(json_file_paths: str, champion_id: int=17):
    tmp = []

    for json_file_path in tqdm(json_file_paths):
        with open(json_file_path, 'r', encoding='utf-8') as f:
            df = json.load(f)

            for participant in df['participants']:
                # print(type(participant['championId']), participant['championId'])

                if participant['championId'] != champion_id:
                    continue

                # print('detected Teemo ^v^')
                role = participant['timeline']['role']
                lane = participant['timeline']['lane']

                if not is_top_role(role, lane):
                    continue

                game_id = extract_game_id(json_file_path)
                participant_id = participant['participantId']
                team_id = participant['teamId']
                win = lose = 0

                for team_info in df['teams']:
                    if team_info['teamId'] == team_id:
                        if team_info['win'] == 'Win':
                            win = 1
                            break

                        else:
                            lose = 1
                            break
                
                # アイテム購入履歴を取得するためのデータを抽出
                tmp.append([game_id, participant_id, win, lose])

    # Counter({'SOLO_TOP': 30, 'DUO_SUPPORT_NONE': 11, 'SOLO_MIDDLE': 5, 'NONE_JUNGLE': 4, 'DUO_MIDDLE': 4, 'DUO_CARRY_BOTTOM': 2, 'DUO_SUPPORT_BOTTOM': 2, 'DUO_TOP': 1}) 
    # print(collections.Counter(tmp))

    np.savetxt(
        'target_data.csv',
        np.array(tmp),
        delimiter=',',
        header='game_id,participant_id,win,lose',
        fmt='%d,%d,%d,%d',
        comments=''
    )
    

if __name__ == '__main__':
    template_file_path = 'C:\output\game\info\*.json'

    json_file_paths = sorted(glob(template_file_path))

    main(json_file_paths)

    print('finished.')