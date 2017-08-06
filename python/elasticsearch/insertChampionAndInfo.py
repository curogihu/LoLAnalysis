import sys
sys.path.append("../collectInformation")
import utility

import json
import os
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

i = 1

def insert_json_to_es(p_f, p_index, p_doc_type):
    i = 1

    json_dict = json.load(p_f)

    for values in json_dict.values():
        es.index(index=p_index, doc_type=p_doc_type, id=i, body=values)
        i += 1


with open(utility.champions_file_path, 'r') as f_json:
    insert_json_to_es(f_json, 'lol_champions', 'champion')

with open(utility.items_file_path, 'r') as f_json:
    insert_json_to_es(f_json, 'lol_items', 'item')



print("ended")



