import json
import os
import numpy as np
import pandas as pd

from glob import glob
from tqdm import tqdm


def main(core_item_keys: np.array, timeline_file_path: str, participant_id: int) -> (int, int):
    tmp = {}

    print('participant_id:', participant_id)

    with open(timeline_file_path, 'r', encoding='utf-8') as f:
        df = json.load(f)

    for frame in df['frames']:
        # print(frame.keys())

        for event in frame['events']:
            # selling items are not taken into consideration.
            if event['type'] not in ['ITEM_PURCHASED', 'ITEM_SOLD']:
                continue

            if event['participantId'] != participant_id:
                continue

            # print(event['itemId'])

            if event['type'] == 'ITEM_PURCHASED':
                if event['itemId'] not in tmp.keys():
                    # print('true pass')
                    tmp[event['itemId']] = [event['timestamp']]

                else:
                    # print('false pass')
                    tmp[event['itemId']].append(event['timestamp'])

                # print(tmp)

            elif event['type'] == 'ITEM_SOLD':
                if event['itemId'] in tmp.keys() and len(tmp[event['itemId']]) > 0:
                    tmp[event['itemId']].pop(0)

    # core_item_cnt = 0
    core_items = []
    

    for item_id, purchase_times in tmp.items():
        if item_id in core_item_keys and len(purchase_times) > 0:
            # core_item_cnt += 1
            core_items.append([item_id, min(purchase_times)])

    # if len(core_items) < 3:
    #     return 0, 0, 0

    if len(core_items) < 2:
        return 0, 0

    core_items_sorted = sorted(core_items, reverse=False, key=lambda x: x[1])

    # print(core_items_sorted)
    # print(core_items_sorted[0][0], core_items_sorted[1][0], core_items_sorted[2][0])

    # return core_items_sorted[:3]

    # return core_items_sorted[0][0], core_items_sorted[1][0], core_items_sorted[2][0]
    return core_items_sorted[0][0], core_items_sorted[1][0]




if __name__ == '__main__':
    np_tmp = np.loadtxt('target_data.csv', delimiter=',', dtype='int64', skiprows=1)
    timeline_file_directory = 'C:\output\game\\timeline'

    core_item_file_path = '../20201229/core_item_data.csv'
    df = pd.read_csv(core_item_file_path)

    core_item_keys = df['item_key'].values
    core_item_names = df['item_name'].values

    core_item_dict = dict(zip(core_item_keys, core_item_names))

    # exit()

    tmp_output = []

    for game_id, participant_id, win, lose in tqdm(np_tmp):
        timeline_file_path = f'{timeline_file_directory}\{game_id}.json'

        item_1, item_2 = main(core_item_keys, timeline_file_path, participant_id)

        if not(item_1 == 0 and item_2 == 0):
            # item_1
            # tmp_output.append([item_1, item_2, win, lose])
            tmp_output.append([core_item_dict[item_1], core_item_dict[item_2], win, lose])

    # np.savetxt(
    #     'item_purchase_history.csv',
    #     np.array(tmp_output),
    #     delimiter=',',
    #     header='item_1,item_2,win,lose',
    #     comments='',
    #     fmt='%d'
    # )

    df_output = pd.DataFrame(np.array(tmp_output), columns=['item_1', 'item_2', 'win', 'lose'])
    df_output.to_csv('item_purchase_history.csv', header=True, index=False, encoding='utf-8')