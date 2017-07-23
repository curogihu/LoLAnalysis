import utility
import json
import os
import sys
from datetime import datetime

# accountIds = open("../output/list/accounts.csv").readlines()

with open(utility.accounts_file_path) as fAccountIds:
    accountIds = fAccountIds.readlines()

cnt = 0
accountIdsLen = len(accountIds)

with open(utility.gameIdsFilePath, 'w', encoding="UTF-8") as fGameIds:

    for accountId in accountIds:
        accountId = accountId.replace("\n", "")

        print("expected account json = " + accountId)

        matchJson = utility.getLoLMatchJson(utility.matchUrl, accountId)

        if matchJson == "" or matchJson == "429":
            print("get json value is [" + matchJson + "]")
            print("Unexpectational error, so it ended.")
            # sys.exit()

            continue

        cnt += 1

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(accountIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        for match in matchJson["matches"]:
            # print(str(match["gameId"]))
            fGameIds.write(str(match["gameId"]) + "\n")

# delete duplicate ids
utility.deleteDuplicatedRecords(utility.gameIdsFilePath, False)