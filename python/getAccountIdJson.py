import utility
from datetime import datetime

with open("../output/list/summoners.csv") as fSummoners:
    summonerIds = fSummoners.readlines()

cnt = 0
summonerIdsLen = len(summonerIds)

with open(utility.accountsFilePath, 'w', encoding="UTF-8") as faccounts:

    for summonerId in summonerIds:
        summonerId = summonerId.replace("\n", "")

        print("expected summonerId json = " + summonerId)
        accountJson = utility.getLoLAccountJson(utility.accountUrl, str(summonerId))

        if accountJson == "" or accountJson == "429":
            print("skipped summonerId json = " + summonerId)

        else:
            faccounts.write(str(accountJson["accountId"]) + "\n")



        cnt += 1

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

"""
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
            continue
            # sys.exit()

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
"""