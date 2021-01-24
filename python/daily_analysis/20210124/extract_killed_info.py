import numpy as np
import pandas as pd
import json
import os
import matplotlib.pyplot as plt

from glob import glob
from tqdm import tqdm




# frames -> event

def main(target: np.ndarray, dict_path: str) -> list:
    results = []

    for json_path, participantId, _ in tqdm(target):
        with open(dict_path + json_path, 'r', encoding='utf-8') as f:
            df = json.load(f)

        # print(dict_path + json_path)

        for frame in df['frames']:
            if not 'events' in frame:
                continue

            for event in frame['events']:
                if event['type'] == 'CHAMPION_KILL':
                    # print(type(event['victimId']), type(participantId))

                    if event['victimId'] == int(participantId):
                        results.append(
                            [
                                int(event['timestamp'] / 1000),
                                event['position']['x'],
                                event['position']['y'],
                                len(event['assistingParticipantIds'])
                            ]
                        )

    # print(results)
    # print('-' * 40)
    # print(sorted(results, key=lambda x: x[0]))

    return np.array(sorted(results, key=lambda x: x[0]))


def print_graphs(results: np.ndarray, image_filename: str):
    fig = plt.figure()

    ax = fig.add_subplot(111, xlabel='Vertical', ylabel='Horizontal')
    ax.scatter(results[:, 1], results[:, 2], c='blue')

    plt.xlim(0, 12500)
    plt.ylim(0, 15000)

    fig.savefig(image_filename)


if __name__ == '__main__':
    npy_target = np.load('lose_match.npy')
    timeline_dict_path = 'C:/output/game/timeline/'
    results = main(npy_target, timeline_dict_path)
    np.save('killed_info', results)

    results = np.load('killed_info.npy')

    # rows = np.where(results[:, 0] <= 900)

    less_than_15_min =  np.where(results[:, 0] < 900)
    more_than_15_min =  np.where(results[:, 0] > 900)
    more_than_20_min =  np.where(results[:, 0] > 1200)
    more_than_25_min =  np.where(results[:, 0] > 1500)
    more_than_30_min =  np.where(results[:, 0] > 1800)

    a = results[less_than_15_min, :]
    b = results[more_than_15_min, :]
    c = results[more_than_20_min, :]
    d = results[more_than_25_min, :]
    e = results[more_than_30_min, :]

    print(a)


    print_graphs(a[0], '0015.png')
    print_graphs(b[0], '1520.png')
    print_graphs(c[0], '2025.png')
    print_graphs(d[0], '2530.png')
    print_graphs(e[0], '3099.png')

    print('finished.')