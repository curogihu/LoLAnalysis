import utility
import json
import os
import sys
from datetime import datetime

# accountIds = open("../output/list/accounts.csv").readlines()

with open("../output/list/accounts.csv").readlines() as fAccountIds:
    accountIds = fAccountIds.readlines()

cnt = 0
accountIdsLen = len(accountIds)

with open(utility.accountsFilePath, 'w', encoding="UTF-8") as fAccounts:

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

        with open(utility.matchDirectoryPath + accountId + ".json", "w") as fjson:
            try:
               # json.dump(gameJson, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
               json.dump(matchJson, fjson, separators=(',', ': '))
            except UnicodeEncodeError as e:
                print("UnicodeEncodeError [getMatchjson] accountId = " + accountId)
                # give up getting json
