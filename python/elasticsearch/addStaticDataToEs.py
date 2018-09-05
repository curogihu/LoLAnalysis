import sys
import json

sys.path.append('../collectInformation')
import utility

# print(utility.champions_file_path)

from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
i = 1

with open(utility.champions_file_path, 'r') as f_champions:
    champions_json = json.load(f_champions)

    for champion_json in champions_json.values():
        es.index(index='champions', doc_type='champion', id=i, body=champion_json)
        i += 1

with open(utility.items_file_path, 'r') as f_items:
    items_json = json.load(f_items)

    for item_json in items_json.values():
        es.index(index='items', doc_type='item', id=i, body=item_json)
        i += 1
        print(i)

