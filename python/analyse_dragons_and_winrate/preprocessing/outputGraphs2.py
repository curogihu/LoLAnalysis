import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

input_merged_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "merged_two_logs_with_champion2.csv")

df = pd.read_csv(input_merged_file_path)

for champion in df["id"].unique():
    # 1. relation of elite monster type, mean of win rate and killed amount
    sns.set(rc={"figure.figsize": (11, 9)})
    sns.barplot(x="win_flag", y="boss_type", hue="amount", data=df[df["id"].str.contains(champion.strip())])
    #    # sns.plt.show()
    plt.savefig(champion.strip() + "_relation_of_elite_moster_and_killed_amount.png")

