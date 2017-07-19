import os
import apiKey as a
from time import sleep
import requests

# DEPRECATED on July 24th, 2017
# challengersUrl = "https://na.api.pvp.net/api/lol/na/v2.5/league/challenger?type=RANKED_SOLO_5x5&api_key=[APIKEY]"
# mastersUrl = "https://na.api.pvp.net/api/lol/na/v2.5/league/master?type=RANKED_SOLO_5x5&api_key=[APIKEY]"
challengersUrl = "https://na1.api.riotgames.com/lol/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=[APIKEY]"
mastersUrl = "https://na1.api.riotgames.com/lol/league/v3/masterleagues/by-queue/RANKED_SOLO_5x5?api_key=[APIKEY]"

# DEPRECATED on July 24th, 2017
# newMatchListUrl = "https://na.api.pvp.net/api/lol/na/v1.3/game/by-summoner/[SUMMONERID]/recent?api_key=[APIKEY]"
accountUrl = "https://na1.api.riotgames.com/lol/summoner/v3/summoners/[SUMMONERID]?api_key=[APIKEY]"
matchUrl = "https://na1.api.riotgames.com/lol/match/v3/matchlists/by-account/[ACCOUNTID]?endIndex=100&beginIndex=0&api_key=[APIKEY]"

# DEPRECATED on July 24th, 2017
# gameUrl = "https://na.api.pvp.net/api/lol/na/v2.2/match/[GAMEID]?includeTimeline=True&api_key=[APIKEY]"

gameInfoUrl = "https://na1.api.riotgames.com/lol/match/v3/matches/[GAMEID]?api_key=[APIKEY]"
gameTimelineUrl = "https://na1.api.riotgames.com/lol/match/v3/timelines/by-match/[GAMEID]?api_key=[APIKEY]"

rankedGameListUrl = "https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/[SUMMONERID]?rankedQueues=TEAM_BUILDER_RANKED_SOLO&beginTime=1481108400000&beginIndex=0&endIndex=30&api_key=[APIKEY]"

challengerSummonersFilePath = '../output/list/summonerChallenger.csv'
masterSummonersFilePath = '../output/list/summonerMaster.csv'
summonersFilePath = '../output/list/summoners.csv'
accountsFilePath = '../output/list/accounts.csv'

gameSummaryFolderPath = '../output/gameSummary/'
matchVersionDirectoryPath = "../output/game/"
matchDirectoryPath = "../output/match/"
accountFolderPath = "../output/account/"
gameIdsFilePath = '../output/list/gameIds.csv'

def getLoLJson(urlTemplate):
    url = urlTemplate.replace("[APIKEY]", a.apiKey)

    return getJson(url)


def getLoLGameListJson(urlTemplate, summonerId):
    url = urlTemplate.replace("[SUMMONERID]", summonerId)
    url = url.replace("[APIKEY]", a.apiKey)

    return getJson(url)


def getLoLMatchJson(urlTemplate, accountId):
    url = urlTemplate.replace("[ACCOUNTID]", accountId)
    url = url.replace("[APIKEY]", a.apiKey)

    return getJson(url)


def getLoLAccountJson(urlTemplate, summonerId):
    url = urlTemplate.replace("[SUMMONERID]", summonerId)
    url = url.replace("[APIKEY]", a.apiKey)

    return getJson(url)


def getLoLGameInfoJson(urlTemplate, gameId):
    url = urlTemplate.replace("[GAMEID]", gameId)
    url = url.replace("[APIKEY]", a.apiKey)

    return getJson(url)


def getLoLGameTimelineJson(urlTemplate, gameId):
    url = urlTemplate.replace("[GAMEID]", gameId)
    url = url.replace("[APIKEY]", a.apiKey)

    print(url)

    return getJson(url)


def getJson(url):
    cnt = 0
    returnJson = ""

    print(url)

    while True:
        sleep(1.3)

        try:
            r = requests.get(url)

        # in case of disconnection or something
        except Exception as e:
            print("exception args: ", e.args)
            cnt += 1

            if cnt >= 5:
                break

            sleep(10)
            continue

        headers = r.headers

        print("----------------------------------------------------")
        print("status code = " + str(r.status_code))

        # for header in headers:
        #    print("header = " + header + ", value = " + headers[header])

        print("----------------------------------------------------")

        if r.status_code == 200:
            print("x rate limit count = " + headers["X-Rate-Limit-Count"])
            returnJson = r.json()
            break

        # fail due to reading unexpected match code
        # have to add a function for skipping error match code
        elif r.status_code == 404:
            returnJson = ""
            break


        elif r.status_code == 429:
            cnt += 1

            # show to solve the problem
            for header in headers:
                print("header = " + header + ", value = " + headers[header])

            # I have to deal with in a case, status code is 429
            """
            limitType = r.headers["X-Rate-Limit-Type"]
            retryAfter = int(r.headers["Retry-After"])

            print("limit type = " + limitType)
            print("retry after = " + retryAfter)

            sleep(retryAfter + 1)
            """

            # emergency stop
            returnJson = "429"
            break;

        elif r.status_code >= 500 and r.status_code <= 599:
            cnt += 1
            sleep(5)

        else:
            print("status code = " + str(r.status_code))
            returnJson = ""
            break

        if cnt >= 5:
            break

    return returnJson

"""
def getJson(url):
    returnCode = 0
    cnt = 0

    while True:
        cnt += 1
        sleep(1)

        try:
            webURL = urllib.request.urlopen(url)
            returnCode = webURL.getcode()
            returnInfo = webURL.info()

        # in particular return 429, beyond the access limit
        except urllib.error.HTTPError as e:
            # if "X-Rate-Limit-Type" in e:
            data = e.read()
            info = e.info()
            headers = e.headers()

            if "Retry-After" in info:
                waitSeconds = int(e["Retry-After"]) + 1
                sleep(waitSeconds)

            else:
                print("HTTPError [Function Name - getJson] It ended due to HTTPError error.")

#                for sentence in data:
#                    print("value = " + sentence)

                for sentence in data:
                    print("value = " + str(sentence))

                for sentence in info:
                    print("info = " + sentence + ", value = " + str(info[sentence]))

                for sentence in headers:
                    print("info = " + sentence + ", value = " + str(headers[sentence]))

                return ""

        except Exception as e:
            data = e.read()
            info = e.info()

            print("Exception [Function Name - getJson] It ended due to unexpectead error.")

            for sentence in data:
                print("value = " + str(sentence))

            for sentence in info:
                print("value = " + str(sentence))

            return ""

        print("return code = " + str(returnCode) + ", X-Rate-Limit-Count = " + returnInfo["X-Rate-Limit-Count"])

        # Riot API could not accept any response in a short time
        #
        if int(returnCode / 100) == 5:
            sleep(10)
            cnt += 1

            # prevent un-nessesary accessing
            if cnt >= 5:
                break

        else:
            # print("return code = " + str(returnCode) + ", url = " + url)
            break

    if returnCode == 200:
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        return json.loads(data.decode(encoding))
    else:
        print("return code = " + str(returnCode) + ", url = " + url)
        return ""
"""

def deleteDuplicatedRecords(filePath, reverseFlg):

    if os.path.exists(filePath):
        # print("passed")
        uniqRecords = sorted(set(open(filePath).readlines()), reverse=reverseFlg)

        fFile = open(filePath, 'w', encoding="UTF-8")

        for record in uniqRecords:
            fFile.write(record)

        fFile.close()