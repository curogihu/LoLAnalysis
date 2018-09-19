import pandas as pd
import os

input_info_file_path = os.path.join("C:", os.sep, "output", "edit", "info", "info_per_line.csv")
input_timeline_file_path = os.path.join("C:", os.sep, "output", "edit", "timeline", "HadSupportItem.csv")
input_champions_file_path = os.path.join("C:", os.sep, "output", "edit", "static-data", "champions.csv")


output_merged_file_path = os.path.join("C:", os.sep, "output", "edit", "preprocessing", "merged_info_and_timeline.csv")
output_merged_champion_file_path = os.path.join("C:", os.sep, "output", "edit", "preprocessing", "merged_with_champion_name.csv")
output_five_players_per_line_file_path = os.path.join("C:", os.sep, "output", "edit", "preprocessing", "merged_match_info.csv")

df = pd.read_csv(input_info_file_path)
df2 = pd.read_csv(input_timeline_file_path)
df3 = pd.read_csv(input_champions_file_path, encoding='cp932', usecols=[0, 2])
df3.columns = ["championId", "name"]

merged_df = pd.merge(df, df2, on=['gameId', 'participantId'])
merged_df.to_csv(output_merged_file_path, index=False)

merged_df2 = pd.merge(merged_df, df3, on=['championId'])
# チャンピオン名に日本語を含むため、shift_jisで出力
# merged_df2.to_csv(output_merged_champion_file_path, encoding="shift_jis")
merged_df2.to_csv(output_merged_champion_file_path)


cnt = 0
tmp = ""

with open(output_five_players_per_line_file_path, "w") as f_2:
    tmp_keys = ""
    tmp_values = ""

    for i in range(5):
        tmp_keys += ",role_lane{0}".format(i)
        tmp_values += ",championId{0},haveSmite{0},haveSupportItem{0}".format(i)

        # 項目名の出力
    f_2.write(tmp_keys[1:] + tmp_values[:])
    f_2.write("\n")

    tmp_keys = ""
    tmp_values = ""

    for a, b, c, d, e in zip(merged_df['role'], \
                                merged_df['lane'], \
                                merged_df['championId'], \
                                merged_df['haveSmite'], \
                                merged_df['haveSupportItem']):
        tmp_keys += ",{0}_{1}".format(a, b)
        tmp_values += ",{0},{1},{2}".format(c, d, e)
        cnt += 1

        # print(tmp)

        if cnt % 5 == 0:
            # print(tmp[1:])
            f_2.write(tmp_keys[1:] + tmp_values[:])
            f_2.write("\n")

            tmp_keys = ""
            tmp_values = ""

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