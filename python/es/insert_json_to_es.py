import json
import glob
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# jsonFiles = glob.glob("---------/game/info/*.*")


i = 1

"""
for jsonFile in jsonFiles:
#    print(jsonFile)
    with open(jsonFile, 'r') as f:
        # gameJson = json.load(f)
        es.index(index='game_info', doc_type='game_info', id=i, body=json.loads(gameJson))
        i += 1

        print(1)
"""


r = requests.get('https://na1.api.riotgames.com/lol/match/v3/matches/2508434907?api_key=RGAPI-47f731a0-65be-4e8b-b4aa-5cc9ba8fbf3d')
es.index(index='lol_game_info', doc_type='game_info', id=i, body=json.loads(r.content))


print("finished")