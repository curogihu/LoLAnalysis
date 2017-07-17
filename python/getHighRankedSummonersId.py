import utility as util

# Output Master and Challenger summoner ids to a files
# 1. summonerChallenger.csv
# 2. summonerMaster.csv
#
# Then, They are combined to a file, summoners.csv with no duplicated ids

challengerSummonerJson = util.getLoLJson(util.challengersUrl)
masterSummonerJson = util.getLoLJson(util.mastersUrl)

# output challenger ids
with open(util.summonersFilePath, 'w', encoding="UTF-8") as fSummoners:
    if challengerSummonerJson != "":
        with open(util.challengerSummonersFilePath, 'w', encoding="UTF-8") as fChallengers:
            for summoner in challengerSummonerJson["entries"]:
                fChallengers.write(summoner["playerOrTeamId"] + "\n")
                fSummoners.write(summoner["playerOrTeamId"] + "\n")

# output master ids
with open(util.summonersFilePath, 'a', encoding="UTF-8") as fSummoners:
    if masterSummonerJson != "":
        with open(util.masterSummonersFilePath, 'w', encoding="UTF-8") as fMasters:
            for summoner in masterSummonerJson["entries"]:
                fMasters.write(summoner["playerOrTeamId"] + "\n")
                fSummoners.write(summoner["playerOrTeamId"] + "\n")

# delete duplicate ids
util.deleteDuplicatedRecords('../output/list/summoners.csv', False)
