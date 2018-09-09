import json
import os

json_file_path = os.path.join("C:", os.sep, "output", "list", "champions.json")
output_csv_file_path = os.path.join("C:", os.sep, "output", "edit", "static-data", "champions.csv")

output_directory_path = os.path.dirname(output_csv_file_path)

if not os.path.exists(output_directory_path):
    os.makedirs(output_directory_path)

with open(output_csv_file_path, 'w') as csv_f:

    # 項目名の出力
    csv_f.write("key,id,name,image\n")

    with open(json_file_path, 'r', encoding="utf-8") as f:
        json_data = json.load(f)

        for champion in json_data.values():
            # print(champion)

            tmp_champion = {}
            tmp_champion['key'] = champion['key']
            tmp_champion['id'] = champion['id']
            tmp_champion['name'] = champion['name']
            tmp_champion['image'] = champion['image']['full']

            tmp = '{key},{id},{name},{image}'.format(key=tmp_champion['key'],
                                                      id=tmp_champion['id'],
                                                      name=tmp_champion['name'],
                                                      image=tmp_champion['image'])

            csv_f.write(tmp)
            csv_f.write("\n")

print("ended")
