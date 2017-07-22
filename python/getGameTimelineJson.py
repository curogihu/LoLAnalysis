import utility
import json
from datetime import datetime

with open("../output/list/gameIds.csv") as fGameIds:
    gameIds = fGameIds.readlines()

cnt = 0
gameIdsLen = len(gameIds)

for gameId in gameIds:
    gameId = gameId.replace("\n", "")

    print("expected gameId json = " + gameId)
    gameTimelineJson = utility.getLoLGameTimelineJson(utility.gameTimelineDirectoryPath, str(gameId))

    if gameTimelineJson == "" or gameTimelineJson == "429":
        print("skipped summonerId json = " + gameId)
        exit()

    cnt += 1

    if cnt % 10 == 0:
        print(str(cnt) + " / " + str(gameIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))



    print(utility.gameTimelineDirectoryPath + gameId + ".json")

    with open(utility.gameTimelineDirectoryPath + gameId + ".json", "w") as fJson:
        try:
            json.dump(gameTimelineJson, fJson, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getMatchjson] gameId = " + gameId)
            # give up getting json
