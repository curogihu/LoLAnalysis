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
    gameInfoJson = utility.getLoLGameInfoJson(utility.gameInfoUrl, str(gameId))
#    gameTimelineJson = utility.get_lol_game_timeline_json(utility.game_timeline_directory_path, str(gameId))

    if gameInfoJson == "" or gameInfoJson == "429":
        print("skipped summonerId json = " + gameId)
        continue

    cnt += 1

    if cnt % 10 == 0:
        print(str(cnt) + " / " + str(gameIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

    print(utility.gameInfoDirectoryPath + gameId + ".json")

    with open(utility.gameInfoDirectoryPath + gameId + ".json", "w") as fJson:
        try:
            json.dump(gameInfoJson, fJson, separators=(',', ': '))
        except UnicodeEncodeError as e:
            print("UnicodeEncodeError [getMatchjson] gameId = " + gameId)
            # give up getting json
