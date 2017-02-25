import utility as util
import json

# matchListUrl = "https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/77720407/recent?api_key=[APIKEY]"

matchListJson = util.getLoLJson(util.matchListUrl)

fGameIds = open(util.gameIdsFilePath, 'a', encoding="UTF-8")

for game in matchListJson["games"]:
    gameId = str(game["gameId"])
    createDate = str(game["createDate"])
    fGameIds.write(gameId + "\n")

    fjson = open(util.gameSummaryFolderPath + createDate + "-" + gameId + ".json", "w")
    json.dump(game, fjson, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
    fjson.close()

fGameIds.close()
