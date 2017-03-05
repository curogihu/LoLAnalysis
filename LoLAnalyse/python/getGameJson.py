# -*- coding: utf-8 -*-

import utility
import json
import os
import sys
from time import sleep
from datetime import datetime

# gameDf = pd.read_csv("../output/matchList.csv", header=None)
# gameDf.columns=['gameId', 'cretaeDate']
# gameIds = gameDf[0:]["gameId"]

gameIds = open("../output/list/gameIds.csv").readlines()

# print(gameDf[0:]["gameId"])

# gameUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/[GAMEID]?includeTimeline=True&api_key=[APIKEY]"

cnt = 0
gameIdsLen = len(gameIds)

# get each json of game detailed information
for gameId in gameIds:
    gameId = gameId.replace("\n", "")

    # get matchVersion from game json and decide a folder to put each json in the near future
    # "matchVersion": "7.4.176.9828",

    print("expected gameId json = " + gameId)

    if os.path.exists("../output/game/" + gameId + ".json"):
        # exclude from target files
        gameIdsLen -= 1
        print("skipped gameId json = " + gameId + "\n")
        continue

    else:
        # print("we have to create " + gameId + ".csv!")

        gameJson = utility.getLoLGameJson(utility.gameUrl, gameId)

        if gameJson == "" or gameJson == "429":
            print("get json value is [" + gameJson + "]")
            print("Unexpectational error, so it ended.")
            sys.exit()

        cnt += 1

        detailMatchVersion = gameJson["matchVersion"].split(".")
        simpleMatchVersion = str(detailMatchVersion[0]) + "." + str(detailMatchVersion[1])
        matchVersionDirectoryPath = "../output/game/" + simpleMatchVersion

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(gameIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        if not os.path.exists(matchVersionDirectoryPath):
            os.mkdir(matchVersionDirectoryPath)

        fjson = open(matchVersionDirectoryPath + "/" + gameId + ".json", "w")
        # json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

        try:
           # json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
           json.dump(gameJson, fjson, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getGamejson] gameId = " + gameId)
            # give up getting json

        fjson.close()