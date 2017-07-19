import utility
from datetime import datetime

with open("../output/list/summoners.csv") as fSummoners:
    summonerIds = fSummoners.readlines()

cnt = 0
summonerIdsLen = len(summonerIds)

with open(utility.accountsFilePath, 'w', encoding="UTF-8") as fAccounts:

    for summonerId in summonerIds:
        summonerId = summonerId.replace("\n", "")

        print("expected summonerId json = " + summonerId)
        accountJson = utility.getLoLGameTimelineJson(utility.gameTimelineUrl, str(summonerId))

        if accountJson == "" or accountJson == "429":
            print("skipped summonerId json = " + summonerId)

        else:

            fAccounts.write(str(accountJson["accountId"]) + "\n")

        cnt += 1

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
