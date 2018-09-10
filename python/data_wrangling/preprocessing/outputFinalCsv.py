import pandas as pd
import os

input_info_file_path = os.path.join("C:", os.sep, "output", "edit", "info", "info_per_line.csv")
input_timeline_file_path = os.path.join("C:", os.sep, "output", "edit", "timeline", "HadSupportItem.csv")
output_merged_file_path =  os.path.join("C:", os.sep, "output", "edit", "preprocessing", "merged_info_and_timeline.csv")
output_five_players_per_line_file_path =  os.path.join("C:", os.sep, "output", "edit", "preprocessing", "merged_match_info.csv")

df = pd.read_csv(input_info_file_path)
df2 = pd.read_csv(input_timeline_file_path)

merged_df = pd.merge(df, df2, on=['gameId', 'participantId'])

cnt = 0
tmp = ""

with open(output_five_players_per_line_file_path, "w") as f_2:
    tmp = ""

    for i in range(5):
        tmp += ",participantId{0},championId{0},role{0},lane{0},haveSmite{0},haveSupportItem{0}".format(i)

        # 項目名の出力
    f_2.write(tmp[1:])
    f_2.write("\n")

    tmp = ""

    for a, b, c, d, e, f in zip(merged_df['participantId'], merged_df['championId'], merged_df['role'], merged_df['lane'], merged_df['haveSmite'], merged_df['haveSupportItem']):
        tmp += ",{0},{1},{2},{3},{4},{5}".format(a, b, c, d, e, f)
        cnt += 1

        # print(tmp)

        if cnt % 5 == 0:
            # print(tmp[1:])
            f_2.write(tmp[1:])
            f_2.write("\n")

            tmp = ""

print("ended")

"""
with open(output_five_players_per_line_file_path, "w") as f_2:
    tmp = ""

    for i in range(5):
        tmp += ",championId{0},role{0},lane{0},haveSmite{0},haveSupportItem{0}".format(i)

    # 項目名の出力
    f_2.write(tmp[1:])
    f_2.write("\n")

    exit()

    for merged_line in merged_lines:
        tmp = ""
        tmp += ",{line}".format(line=merged_line)

        print(merged_line)
        exit()

        cnt += 1

        if cnt % 5 == 0:
            f_2.write("{tmp}".format(tmp=tmp[1:]))
            tmp = ""
"""