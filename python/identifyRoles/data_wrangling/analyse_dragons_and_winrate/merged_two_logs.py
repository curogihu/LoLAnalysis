import pandas as pd
import os

input_killed_log_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "killed_log.csv")
input_win_team_log_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "win_team_log.csv")

output_merged_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "merged_two_logs.csv")

df = pd.read_csv(input_killed_log_file_path)
df2 = pd.read_csv(input_win_team_log_file_path)

merged_df = pd.merge(df, df2, on=['game_id', 'team_id'])
merged_df.to_csv(output_merged_file_path)