import os
import apiKey as a
from time import sleep
import requests

# server_url = "https://na1.api.riotgames.com/lol"
server_url = "https://jp1.api.riotgames.com/lol"

challengers_url = server_url + "/league/v3/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=[APIKEY]"
masters_url = server_url + "/league/v3/masterleagues/by-queue/RANKED_SOLO_5x5?api_key=[APIKEY]"
account_url = server_url + "/summoner/v3/summoners/[SUMMONERID]?api_key=[APIKEY]"
match_url = server_url + "/match/v3/matchlists/by-account/[ACCOUNTID]?queue=420&season=11&api_key=[APIKEY]"
game_info_url = server_url + "/match/v3/matches/[GAMEID]?api_key=[APIKEY]"
game_timeline_url = server_url + "/match/v3/timelines/by-match/[GAMEID]?api_key=[APIKEY]"

# バージョンはとりあえず決め打ち。　呼び出し元で最新のバージョン取得し、URLを変更する方式に切り替える
champion_url = "http://ddragon.leagueoflegends.com/cdn/8.16.1/data/ja_JP/champion.json"
item_url = "http://ddragon.leagueoflegends.com/cdn/8.16.1/data/ja_JP/item.json"

# https://developer.riotgames.com/static-data.html
# http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json
# http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/item.json


# for Windows setting
# refactoring, path = os.path.join(['C:', 'path', 'to', 'file'])
challenger_summoners_file_path = os.path.join('C:', os.sep, 'output', 'list', 'summonerChallenger.csv')
master_summoners_file_path = os.path.join('C:', os.sep, 'output', 'list', 'summonerMaster.csv')
summoners_file_path = os.path.join('C:', os.sep, 'output', 'list', 'summoners.csv')
accounts_file_path = os.path.join('C:', os.sep, 'output', 'list', 'accounts.csv')
game_ids_file_path = os.path.join('C:', os.sep, 'output', 'list', 'game_ids.csv')
timelines_file_path = os.path.join('C:', os.sep, 'output', 'list', 'timelines.csv')

champions_file_path = os.path.join('C:', os.sep, "output", "list", "champions.json")
items_file_path = os.path.join('C:', os.sep,"output", "list", "items.json")

# I' like to set a path, such as C:/output/game/
match_version_directory_path = os.path.join("C:", os.sep, "output", "game", "")
match_directory_path = os.path.join("C:", os.sep, "output", "match", "")
game_info_directory_path = os.path.join("C:", os.sep, "output", "game", "info", "")
game_timeline_directory_path = os.path.join("C:", os.sep, "output", "game", "timeline", "")
account_folder_path = os.path.join("C:", os.sep, "output", "account", "")

"""
# for Mac setting
# refactoring, path = os.path.join(['C:', 'path', 'to', 'file'])
challenger_summoners_file_path = os.path.join('', os.sep, 'Applications', 'output', 'list', 'summonerChallenger.csv')
master_summoners_file_path = os.path.join('', os.sep, 'Applications', 'output', 'list', 'summonerMaster.csv')
summoners_file_path = os.path.join('', os.sep, 'Applications', 'output', 'list', 'summoners.csv')
accounts_file_path = os.path.join('', os.sep, 'Applications', 'output', 'list', 'accounts.csv')
game_ids_file_path = os.path.join('', os.sep, 'Applications', 'output', 'list', 'game_ids.csv')
timelines_file_path = os.path.join('', os.sep, 'Applications', 'output', 'list', 'timelines.csv')

champions_file_path = os.path.join('', os.sep, 'Applications', "output", "list", "champions.json")
items_file_path = os.path.join('', os.sep, 'Applications', "output", "list", "items.json")

# I'd like to set a path, such as C:/output/game/
match_version_directory_path = os.path.join("", os.sep, 'Applications', "output", "game", "")
match_directory_path = os.path.join("", os.sep, 'Applications', "output", "match", "")
game_info_directory_path = os.path.join("", os.sep, 'Applications', "output", "game", "info", "")
game_timeline_directory_path = os.path.join("", os.sep, 'Applications', "output", "game", "timeline", "")
account_folder_path = os.path.join("", os.sep, 'Applications', "output", "account", "")
"""

# created to search quickly than list object
def get_dict_account_id():

    res_dict = {}

    with open(accounts_file_path) as f:
        for line in f:
            account_id = int(line.replace("\n", ""))
            res_dict[account_id] = account_id

    return res_dict


def get_lol_challenger_summoners_id_json():
    return get_lol_json(challengers_url)


def get_lol_master_summoners_id_json():
    return get_lol_json(masters_url)


def get_lol_json(urlTemplate):
    url = urlTemplate.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_lol_game_list_json(urlTemplate, summonerId):
    url = urlTemplate.replace("[SUMMONERID]", summonerId)
    url = url.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_lol_match_json(urlTemplate, accountId):
    url = urlTemplate.replace("[ACCOUNTID]", accountId)
    url = url.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_lol_account_json(urlTemplate, summonerId):
    url = urlTemplate.replace("[SUMMONERID]", summonerId)
    url = url.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_lol_game_info_json(urlTemplate, gameId):
    url = urlTemplate.replace("[GAMEID]", gameId)
    url = url.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_lol_game_timeline_json(urlTemplate, gameId):
    url = urlTemplate.replace("[GAMEID]", gameId)
    url = url.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_lol_game_champion_info_json():
    url = champion_url.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_lol_item_info_json():
    url = item_url.replace("[APIKEY]", a.apiKey)

    return get_json(url)


def get_json(url):
    cnt = 0
    return_json = ""

    print(url)

    while True:
        sleep(1.5)

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
            if "X-Rate-Limit-Count" in headers:
                print("x rate limit count = " + headers["X-Rate-Limit-Count"])

            return_json = r.json()
            break

        # fail due to reading unexpected match code
        # have to add a function for skipping error match code
        elif r.status_code == 404:
            return_json = ""
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

            sleep(10)

            # emergency stop
            return_json = "429"
            break;

        elif r.status_code >= 500 and r.status_code <= 599:
            cnt += 1
            sleep(5)

        else:
            print("status code = " + str(r.status_code))
            return_json = ""
            break

        if cnt >= 5:
            break

    return return_json

"""
def get_json(url):
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
                print("HTTPError [Function Name - get_json] It ended due to HTTPError error.")

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

            print("Exception [Function Name - get_json] It ended due to unexpectead error.")

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

def delete_duplicated_records(filePath, reverseFlg):

    if os.path.exists(filePath):
        # print("passed")
        uniqRecords = sorted(set(open(filePath).readlines()), reverse=reverseFlg)

        fFile = open(filePath, 'w', encoding="UTF-8")

        for record in uniqRecords:
            fFile.write(record)

        fFile.close()
