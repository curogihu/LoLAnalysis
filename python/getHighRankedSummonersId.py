import utility as util

challengerSummonerJson = util.getLoLJson(util.challengersUrl)
masterSummonerJson = util.getLoLJson(util.mastersUrl)

fChallengers = open(util.challengerSummonersFilePath, 'w', encoding="UTF-8")
fMasters = open(util.masterSummonersFilePath, 'w', encoding="UTF-8")
fSummoners = open(util.summonersFilePath, 'a', encoding="UTF-8")

for summoner in challengerSummonerJson["entries"]:
    fChallengers.write(summoner["playerOrTeamId"] + "\n")
    fSummoners.write(summoner["playerOrTeamId"] + "\n")

for summoner in masterSummonerJson["entries"]:
    fMasters.write(summoner["playerOrTeamId"] + "\n")
    fSummoners.write(summoner["playerOrTeamId"] + "\n")

fChallengers.close()
fMasters.close()
fSummoners.close()

util.deleteDuplicatedRecords('../output/list/summoners.csv')