import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

input_file_path = os.path.join("C:", os.sep, "output", "edit", "preprocessing", "merged_match_info.csv")

df = pd.read_csv(input_file_path)
df_train, df_test = train_test_split(df, test_size=0.3)

features = df.columns[5:]

print(features)

forest = RandomForestClassifier(n_estimators=10)
forest.fit(df_train[features])

"""
print(len(df))
print(len(df_train))
print(len(df_test))
"""

"""
colsRes = ['role_lane0','role_lane1','role_lane2','role_lane3','role_lane4']
X_train = train.drop(colsRes, axis = 1)
Y_train = pd.DataFrame(train[colsRes])
rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, Y_train)
"""

# forest = RandomForestClassifier(n_estimators=10)
# forest.fit(df_train, df_test)