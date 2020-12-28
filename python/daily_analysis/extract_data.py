import numpy as np
import json

from glob import glob
from tqdm import tqdm

import matplotlib.pyplot as plt


def main(json_paths: list) -> np.array:
    game_durations = []

    for json_path in tqdm(json_paths):
        with open(json_path) as f:
            df = json.load(f)

            game_durations.append(df['gameDuration'])

    return np.array(game_durations)


if __name__ == "__main__":
    # base_template_path = 'C:\output\game\info\*.json'

    # json_paths = sorted(glob(base_template_path))

    # game_durations = main(json_paths)
    # np.save('high_ranked_match_durations', game_durations)

    game_durations = np.load('high_ranked_match_durations.npy')
    game_durations_adjusted = game_durations // 60

    plt.hist(game_durations_adjusted, bins=20)
    plt.savefig('tmp.png')