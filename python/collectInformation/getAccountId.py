from datetime import datetime

import utility

with open(utility.summoners_file_path) as fSummoners:
    summonerIds = fSummoners.readlines()

cnt = 0
summonerIdsLen = len(summonerIds)

with open(utility.accounts_file_path, 'w', encoding="UTF-8") as fAccounts:

    for summonerId in summonerIds:
        summonerId = summonerId.replace("\n", "")

        print("expected summonerId json = " + summonerId)
        accountJson = utility.get_lol_account_json(utility.account_url, str(summonerId))

        if accountJson == "" or accountJson == "429":
            print("skipped summonerId json = " + summonerId)

        else:
            fAccounts.write(str(accountJson["accountId"]) + "\n")

        cnt += 1

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
