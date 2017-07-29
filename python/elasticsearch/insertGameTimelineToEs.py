import json
import os
import glob
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# f = open('test.json', 'r')
# json_dict = json.load(f)

"""
r = requests.get('http://localhost:9200')
i = 1

while r.status_code == 200:
    r = requests.get('http://swapi.co/api/people/'+ str(i))
    es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
    i = i + 1

print(i)
"""

# files = glob.glob('C:\Python25\*.*') # ワイルドカードが使用可能
# i = 1

#for file in files:
#    print file

files = glob.glob(os.path.join("C:", os.sep, "output", "game", "timeline", "*.json"))
i = 1

for file in files:
    f = open(file, 'r')
    json_dict = json.load(f)

    es.index(index='lol_timeline', doc_type='timeline', id=i, body=json_dict)
    print("success: " + str(i))
    i += 1

print("ended")
