import json
import os
import glob
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "timeline", "*.json"))

i = 1
json_docs = []

for file_path in files_path:
    game_id, ext = os.path.splitext(os.path.basename(file_path))

    with open(file_path, 'r') as f:
        json_data = json.load(f)
        f_1 = json_data['frames']

        # print(f_1)
        for tmp in f_1:
            if tmp['events']:
                tmp_events = tmp['events']

                for tmp_event in tmp_events:
                    if tmp_event['type'] == 'ITEM_PURCHASED':
                        tmp_event['gameId'] = game_id

                        es.index(index='lol_item_builds', doc_type='item_build', id=i, body=tmp_event)

                        print(i)
                        i += 1

print("ended")
