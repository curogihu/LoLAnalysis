import utility
import json
import os
import sys
from datetime import datetime

# gameDf = pd.read_csv("../output/matchList.csv", header=None)
# gameDf.columns=['gameId', 'cretaeDate']
# gameIds = gameDf[0:]["gameId"]

accountIds = open("../output/list/accounts.csv").readlines()

# print(gameDf[0:]["gameId"])

# gameUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/[GAMEID]?includeTimeline=True&api_key=[APIKEY]"

# replace to https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/36930?endIndex=100&beginIndex=0&api_key=[APIKEY]

cnt = 0
accountIdsLen = len(accountIds)

if not os.path.exists(utility.matchDirectoryPath):
    os.mkdir(utility.matchDirectoryPath)

# get each json of game detailed information
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
