import utility as util
import json
import os
import sys
import time
from time import sleep
from datetime import datetime

currentTimeStamp = int(time.time() * 1000)
timeStamp2Weeks = 1209600000
timeStampLimit = currentTimeStamp - timeStamp2Weeks

summonersId = open("../output/list/summoners.csv").readlines()

# print(summonersId)
cnt = 0
summonersLen = str(len(summonersId))

for summonerId in summonersId:
    # have to delete new line code
    summonerId = summonerId.replace("\n", "")
    cnt += 1

    if cnt % 10 == 0:
        print(str(cnt) + " / " + summonersLen + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    gameListJson = util.getLoLGameListJson(util.rankedGameListUrl, summonerId)

    if gameListJson == "":
        sys.exit()

    fGameIds = open(util.gameIdsFilePath, 'a', encoding="UTF-8")

    for match in gameListJson["matches"]:
        matchTimeStamp = match["timestamp"]

        if timeStampLimit > matchTimeStamp:
            break

        gameId = str(match["matchId"])
        fGameIds.write(gameId + "\n")

fGameIds.close()

util.deleteDuplicatedRecords(util.gameIdsFilePath)
