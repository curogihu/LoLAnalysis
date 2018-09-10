import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

input_five_players_per_line_file_path = os.path.join("C:", os.sep, "output", "edit", "preprocessing", "merged_match_info.csv")

df = pd.read_csv(input_five_players_per_line_file_path)
df_train, df_test = train_test_split(df, test_size=0.3)


print(len(df))
print(len(df_train))
print(len(df_test))