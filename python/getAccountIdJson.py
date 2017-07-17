import utility
import os
import sys
import json
from datetime import datetime

summonerIds = open("../output/list/summoners.csv").readlines()

cnt = 0
summonerIdsLen = len(summonerIds)

for summonerId in summonerIds:
    summonerId = summonerId.replace("\n", "")

    print("expected summonerId json = " + summonerId)

    if os.path.exists(utility.accountFolderPath + summonerId + ".json"):
        # exclude from target files
        summonerIdsLen -= 1
        print("skipped gameId json = " + str(summonerId) + "\n")
        continue

    else:
        accountJson = utility.getLoLAccountJson(utility.accountUrl, str(summonerIdsLen))

        if accountJson == "" or accountJson == "429":
            print("get json value is [" + accountJson + "]")
            print("Unexpectational error, so it ended.")
            sys.exit()

        cnt += 1

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        if not os.path.exists(utility.accountFolderPath):
            os.mkdir(utility.accountFolderPath)

        # fjson = open(utility.accountFolderPath + summonerId + ".json", "w")

        with open(utility.accountFolderPath + summonerId + ".json", "w") as fjson:

        try:
            json.dump(accountJson, fjson, separators=(',', ': '))

        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getGamejson] gameId = " + summonerId)
            # give up getting json

        # fjson.close()