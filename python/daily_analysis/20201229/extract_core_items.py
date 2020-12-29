import numpy as np
import json

import pandas as pd

from tqdm import tqdm


def output_core_item_info(json_path: str):
    with open(json_path, 'r', encoding='utf-8') as f:
        df = json.load(f)

    tmp = []

    for item_key, item_data in tqdm(df.items()):
        # skip base item
        if 'into' in item_data.keys():
            continue

        # skip doran items and something
        if 'depth' not in item_data.keys():
            continue

        """
        2033: コラプトポーション
        3041: メジャイ
        """
        if item_key in ['2033', '3041']:
            continue

        tmp.append([item_key, item_data['name'], item_data['image']['full'], item_data['gold']['total']])


    df_output = pd.DataFrame(np.array(tmp), columns=['item_key', 'item_name', 'item_image', 'needed_gold'])
    df_output.to_csv('item_data.csv', header=True, index=False, encoding='utf-8')


if __name__ == '__main__':
    item_json_file_path = 'C:\output\list\items.json'

    output_core_item_info(item_json_file_path)

    print('finished outputting core items file.')