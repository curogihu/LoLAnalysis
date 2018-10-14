import pandas as pd
import os

# from python.analyse_dragons_and_winrate import path_utility as pu

input_killed_log_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "killed_log.csv")
input_win_team_log_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "win_participant_log.csv")
input_champion_file_path = os.path.join("C:", os.sep, "output", "edit", "static-data", "champions.csv")

output_merged_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "merged_two_logs_with_champion.csv")
output_merged_file_path2 = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "merged_two_logs_with_champion2.csv")

df = pd.read_csv(input_killed_log_file_path)
df2 = pd.read_csv(input_win_team_log_file_path)

merged_df = pd.merge(df, df2, on=['game_id', 'team_id'])
merged_df.to_csv(output_merged_file_path, index=False, columns=["boss_type", "key", "time", "amount", "win_flag", "total_time"])

df3 = pd.read_csv(input_champion_file_path, encoding='cp932')
df4 = pd.read_csv(output_merged_file_path)
merged_df2 = pd.merge(df4, df3, on="key")
merged_df2.to_csv(output_merged_file_path2, index=False, columns=["boss_type", "id", "time", "amount", "win_flag", "total_time"])


# print(len(merged_df.game_id.unique()))
# print(len(merged_df2.game_id.unique()))

# print(merged_df.head)
# print(df3.head)