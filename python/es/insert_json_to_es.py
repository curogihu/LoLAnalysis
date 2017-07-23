import json
import glob
import requests
from elasticsearch import Elasticsearch

"""
import os, sys
print(os.getcwd())
sys.path.append(os.getcwd())
"""

import utility
import apiKey as a

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# jsonFiles = glob.glob("---------/game/info/*.*")


with open("../output/list/game_ids.csv") as fGameIds:
    gameIds = fGameIds.readlines()

cnt = 0
gameIdsLen = len(gameIds)

i = 1

for gameId in gameIds:
    gameId = gameId.replace("\n", "")

    print("expected game_id json = " + gameId)
    gameInfoJson = utility.getLoLGameInfoJson(utility.gameInfoUrl, str(gameId))

    url = utility.gameInfoUrl.replace("")
    url = url.replace("[GAMEID]", gameId)
    url = url.replace("[APIKEY]", a.apiKey)

    r = requests.get(url)
    es.index(index='lol_game_info', doc_type='game_info', id=i, body=json.loads(r.content))

    if cnt % 10 == 0:
        print(str(cnt) + " / " + str(gameIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    cnt+=1
    i+=1

print("finished")