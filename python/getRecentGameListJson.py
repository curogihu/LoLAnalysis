import utility as util
import json
import os
import sys
from time import sleep
from datetime import datetime

# matchListUrl = "https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/77720407/recent?api_key=[APIKEY]"
summonersId = open("../output/list/summoners.csv").readlines()

# print(summonersId)
cnt = 0
summonersLen = str(len(summonersId))

for summonerId in summonersId:
    # have to delete new line code
    summonerId = summonerId.replace("\n", "")
    # url = util.getLoLGameListJson(util.newMatchListUrl, summonerId)
    cnt += 1

    # print("i = " + str(i) + ", id = [" + summonerId + "]")

    if cnt % 10 == 0:
        print(str(cnt) + " / " + summonersLen + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    gameListJson = util.getLoLGameListJson(util.newMatchListUrl, summonerId)

    if gameListJson == "":
        sys.exit()

    fGameIds = open(util.gameIdsFilePath, 'a', encoding="UTF-8")

    for game in gameListJson["games"]:
        gameId = str(game["gameId"])
#        createDate = str(game["createDate"])

        # preparation for getting detailed game information
        fGameIds.write(gameId + "\n")

        # output game Summary Json, not necessary?
        # gameSummaryFilePath = util.gameSummaryFolderPath + createDate + "-" + gameId + ".json"
        gameSummaryFilePath = util.gameSummaryFolderPath + gameId + ".json"

        if not os.path.exists(gameSummaryFilePath):
            fjson = open(gameSummaryFilePath, "w")
            # json.dump(game, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
            json.dump(game, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
            fjson.close()

fGameIds.close()

util.deleteDuplicatedRecords(util.gameIdsFilePath, True)
