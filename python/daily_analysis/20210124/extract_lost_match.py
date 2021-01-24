import numpy as np
import json
import os

from glob import glob


# レネクトンのidは58
def main(json_paths: list, target_summoner_name: str) -> list:
    results = []
    
    for json_path in json_paths:
        with open(json_path, 'r', encoding='utf-8') as f:
            df = json.load(f)
            participantId = -1

            for participantIdenty in df['participantIdentities']:
                summoner_name = participantIdenty['player']['summonerName']

                # print(summoner_name, summoner_name == target_summoner_name)

                if summoner_name == target_summoner_name:
                    participantId = participantIdenty['participantId']
                    break

            # could not find summoner name
            if participantId == -1:
                continue

            target_participant = df['participants'][participantId - 1]

            if 1 <= participantId <= 5:
                results.append([os.path.basename(json_path), participantId, target_participant['stats']['win']])

    return results


if __name__ == "__main__":
    json_format_path = 'C:/output/game/info/*.json'
    target_summoner_name = 'とりしあ'
    json_paths = sorted(glob(json_format_path))

    results = main(json_paths, target_summoner_name)

    np.save('lose_match', results)

    print('finished')

    # print(results)


    # for x, y in results:
    #     print(x, y)



