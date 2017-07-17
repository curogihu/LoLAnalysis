import utility
import os
import sys
import json
from datetime import datetime

summonerIds = open("../output/list/summoners.csv").readlines()

# print(gameDf[0:]["gameId"])

# gameUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/[GAMEID]?includeTimeline=True&api_key=[APIKEY]"

cnt = 0
summonerIdsLen = len(summonerIds)

# get each json of game detailed information
for summonerId in summonerIds:
    summonerId = summonerId.replace("\n", "")

    # get matchVersion from game json and decide a folder to put each json in the near future
    # "matchVersion": "7.4.176.9828",

    print("expected summonerId json = " + summonerId)

    if os.path.exists(utility.accountFolderPath + summonerId + ".json"):
        # exclude from target files
        summonerIdsLen -= 1
        print("skipped gameId json = " + str(summonerId) + "\n")
        continue

    else:
        # print("we have to create " + gameId + ".csv!")

        accountJson = utility.getLoLAccountJson(utility.accountUrl, str(summonerIdsLen))

        if accountJson == "" or accountJson == "429":
            print("get json value is [" + accountJson + "]")
            print("Unexpectational error, so it ended.")
            sys.exit()

        cnt += 1

        # detailMatchVersion = gameJson["matchVersion"].split(".")
        #  simpleMatchVersion = str(detailMatchVersion[0]) + "." + str(detailMatchVersion[1])
        # matchVersionDirectoryPath = "../output/game/" + simpleMatchVersion
        # matchVersionDirectoryPath = "../output/game/" + simpleMatchVersion

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        if not os.path.exists(utility.accountFolderPath):
            os.mkdir(utility.accountFolderPath)

        fjson = open(utility.accountFolderPath + summonerId + ".json", "w")
        # json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))

        try:
            # json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
            json.dump(accountJson, fjson, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getGamejson] gameId = " + summonerId)
            # give up getting json

        fjson.close()