import json
import os

json_file_path = os.path.join("C:", os.sep, "output", "list", "items.json")
output_csv_file_path = os.path.join("C:", os.sep, "output", "edit", "static-data", "items.csv")
output_csv_derivation_file_path = os.path.join("C:", os.sep, "output", "edit", "static-data", "items_derivation.csv")

output_directory_path = os.path.dirname(output_csv_file_path)

if not os.path.exists(output_directory_path):
    os.makedirs(output_directory_path)

with open(output_csv_file_path, 'w', encoding="utf-8") as csv_f:
    with open(output_csv_derivation_file_path, 'w', encoding="utf-8") as csv_derivation_f:

        # 項目名の出力
        csv_f.write("key,name,depth,description,total_price,sell_price,image\n")
        csv_derivation_f.write("key,derived\n")

        with open(json_file_path, 'r', encoding="utf-8") as f:
            json_data = json.load(f)

            for k, v in json_data.items():
                # print(v)

                tmp_item = {}
                tmp_item['key'] = k
                tmp_item['name'] = v['name']

                if 'depth' in v:
                    tmp_item['depth'] = v['depth']

                else:
                    tmp_item['depth'] = 1

                tmp_item['description'] = v['description']
                tmp_item['total_price'] = v['gold']['total']
                tmp_item['sell_price'] = v['gold']['sell']
                tmp_item['image'] = v['image']['full']

                tmp = '{key},{name},{depth},{description},{total_price}, {sell_price}, {image}\n'.format(key=tmp_item['key'],
                                                                                               name=tmp_item['name'],
                                                                                               depth=tmp_item['depth'],
                                                                                               description=tmp_item['description'],
                                                                                               total_price=tmp_item['total_price'],
                                                                                               sell_price=tmp_item['sell_price'],
                                                                                               image=tmp_item['image'])
                csv_f.write(tmp)

                if 'from' in v:
                    sorted_forms = sorted(v['from'])

                    for derived_item in sorted_forms:
                        tmp_derivation = '{key}, {derived}\n'.format(key=tmp_item['key'],
                                                                     derived=derived_item)
                        csv_derivation_f.write(tmp_derivation)


print("ended")
