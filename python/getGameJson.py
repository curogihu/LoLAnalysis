import utility
import json
import pandas as pd
import os

gameDf = pd.read_csv("../output/matchList.csv", header=None)
gameDf.columns=['gameId', 'cretaeDate']
gameIds = gameDf[0:]["gameId"]

# print(gameDf[0:]["gameId"])

gameUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/[GAMEID]?includeTimeline=True&api_key=[APIKEY]"
apiKey = "RGAPI-dbaaf04c-e2b6-4c54-a8bc-9910e003fdbd"

# get each json of game detailed information
for gameId in gameIds:
    gameId = str(gameId)

    if not os.path.exists("../output/game/" + gameId + ".json"):
        # print("we have to create " + gameId + ".csv!")

        gameJson = utility.getLoLGameJson(gameUrl, gameId)

        fjson = open("../output/game/" + gameId + ".json", "w")
        json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        fjson.close()