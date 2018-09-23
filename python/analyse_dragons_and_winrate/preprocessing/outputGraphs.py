import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

# output_merged_file_path = os.path.join("", os.sep, "Applications", "output", "edit", "boss_killed_log", "merged_two_logs.csv")
output_merged_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "merged_two_logs.csv")

df = pd.read_csv(output_merged_file_path)

# 1. relation of elite monster type, mean of win rate and killed amount
sns.set(rc={"figure.figsize": (11, 9)})
sns.barplot(x="win_flag", y="boss_type", hue="amount", data=df)
#    # sns.plt.show()
plt.savefig("relation_of_elite_moster_and_killed_amount.png")

# 2. relation of elite monster type, mean of killed time and killed amount
sns.barplot(x="time", y="boss_type", hue="amount", data=df)
plt.savefig("relation_of_elite_monster_and_killed_time.png")
