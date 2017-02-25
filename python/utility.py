import json
import urllib.request
import os
import apiKey as a

challengersUrl = "https://na.api.pvp.net/api/lol/na/v2.5/league/challenger?type=RANKED_SOLO_5x5&api_key=[APIKEY]"
mastersUrl = "https://na.api.pvp.net/api/lol/na/v2.5/league/master?type=RANKED_SOLO_5x5&api_key=[APIKEY]"
matchListUrl = "https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/77720407/recent?api_key=[APIKEY]"

challengerSummonersFilePath = '../output/list/summonerChallenger.csv'
masterSummonersFilePath = '../output/list/summonerMaster.csv'
summonersFilePath = '../output/list/summoners.csv'
gameSummaryFolderPath = '../output/gameSummary/'
gameIdsFilePath = '../output/list/gameIds.csv'

def getLoLJson(urlTemplate):
    url = urlTemplate.replace("[APIKEY]", a.apiKey)
    webURL = urllib.request.urlopen(url)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))

def getLoLGameJson(urlTemplate, gameId):
    url = urlTemplate.replace("[GAMEID]", gameId)
    url = url.replace("[APIKEY]", a.apiKey)

    webURL = urllib.request.urlopen(url)
    data = webURL.read()
    encoding = webURL.info().get_content_charset('utf-8')
    return json.loads(data.decode(encoding))

def deleteDuplicatedRecords(filePath):

    if os.path.exists(filePath):
        # print("passed")
        uniqRecords = sorted(set(open(filePath).readlines()))

        fFile = open(filePath, 'w', encoding="UTF-8")

        for record in uniqRecords:
            fFile.write(record)

        fFile.close()