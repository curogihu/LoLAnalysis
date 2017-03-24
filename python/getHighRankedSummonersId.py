import utility as util

challengerSummonerJson = util.getLoLJson(util.challengersUrl)
masterSummonerJson = util.getLoLJson(util.mastersUrl)

fSummoners = open(util.summonersFilePath, 'w', encoding="UTF-8")

if challengerSummonerJson != "":
    fChallengers = open(util.challengerSummonersFilePath, 'w', encoding="UTF-8")

    for summoner in challengerSummonerJson["entries"]:
        fChallengers.write(summoner["playerOrTeamId"] + "\n")
        fSummoners.write(summoner["playerOrTeamId"] + "\n")

    fChallengers.close()

if masterSummonerJson != "":
    fMasters = open(util.masterSummonersFilePath, 'w', encoding="UTF-8")

    for summoner in masterSummonerJson["entries"]:
        fMasters.write(summoner["playerOrTeamId"] + "\n")
        fSummoners.write(summoner["playerOrTeamId"] + "\n")

    fMasters.close()

fSummoners.close()

util.deleteDuplicatedRecords('../output/list/summoners.csv', False)