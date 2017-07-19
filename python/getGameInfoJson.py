import utility
from datetime import datetime

with open("../output/list/gameIds.csv") as fGameIds:
    gameIds = fGameIds.readlines()

cnt = 0
summonerIdsLen = len(gameIds)


    for summonerId in gameIds:
        summonerId = summonerId.replace("\n", "")

        print("expected summonerId json = " + summonerId)
        accountJson = utility.getLoLGameInfoJson(utility.gameInfoUrl, str(summonerId))

        if accountJson == "" or accountJson == "429":
            print("skipped summonerId json = " + summonerId)

        else:
            fAccounts.write(str(accountJson["accountId"]) + "\n")

        cnt += 1

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
