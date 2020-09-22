import json, os
# from datetime import datetime

import datetime
import time
import math

import utility


def get_high_ranked_summoner_ids():
    challenger_summoner_json = utility.get_lol_challenger_summoners_id_json()
    grandmaster_summoner_json = utility.get_lol_grandmaster_summoners_id_json()
    master_summoner_json = utility.get_lol_master_summoners_id_json()

    # output challenger ids
    with open(utility.summoners_file_path, 'w', encoding="UTF-8") as f_summoners:
        if challenger_summoner_json != "":
            with open(utility.challenger_summoners_file_path, 'w', encoding="UTF-8") as f_challengers:
                for summoner in challenger_summoner_json["entries"]:
                    f_challengers.write(summoner["summonerId"] + "\n")
                    f_summoners.write(summoner["summonerId"] + "\n")

    # output grandmaster ids
    with open(utility.summoners_file_path, 'a', encoding="UTF-8") as f_summoners:
        if grandmaster_summoner_json != "":
            with open(utility.grandmaster_summoners_file_path, 'w', encoding="UTF-8") as f_grandMasters:
                for summoner in grandmaster_summoner_json["entries"]:
                    f_grandMasters.write(summoner["summonerId"] + "\n")
                    f_summoners.write(summoner["summonerId"] + "\n")

    # output master ids
    with open(utility.summoners_file_path, 'a', encoding="UTF-8") as f_summoners:
        if master_summoner_json != "":
            with open(utility.master_summoners_file_path, 'w', encoding="UTF-8") as f_masters:
                for summoner in master_summoner_json["entries"]:
                    f_masters.write(summoner["summonerId"] + "\n")
                    f_summoners.write(summoner["summonerId"] + "\n")


    # make unique summoner ids in a file
    utility.delete_duplicated_records(utility.summoners_file_path, False)


def get_account_ids():
    with open(utility.summoners_file_path) as fSummoners:
        summonerIds = fSummoners.readlines()

    cnt = 0
    summonerIdsLen = len(summonerIds)

    with open(utility.accounts_file_path, 'w', encoding="UTF-8") as fAccounts:

        for summonerId in summonerIds:
            summonerId = summonerId.replace("\n", "")

            print("expected summonerId json = " + summonerId)
            accountJson = utility.get_lol_account_json(utility.account_url, str(summonerId))

            if accountJson == "" or accountJson == "429":
                print("skipped summonerId json = " + summonerId)

            else:
                fAccounts.write(str(accountJson["accountId"]) + "\n")

            cnt += 1

            if cnt % 10 == 0:
                # print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                print('{0} / {1}, {2}'.format(cnt, summonerIdsLen, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))


def get_game_ids():
    with open(utility.accounts_file_path) as f_account_ids:
        account_ids = f_account_ids.readlines()

    cnt = 0
    account_ids_len = len(account_ids)

    with open(utility.game_ids_file_path, 'w', encoding="UTF-8") as f_game_ids:

        for account_id in account_ids:
            account_id = account_id.replace("\n", "")

            print("expected account json = " + account_id)

            match_json = utility.get_lol_match_json(utility.match_url, account_id)

            if match_json == "" or match_json == "429":
                print("get json value is [" + match_json + "]")
                print("Unexpectational error, so it ended.")
                # sys.exit()

                continue

            cnt += 1

            if cnt % 10 == 0:
                # print(str(cnt) + " / " + str(account_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
                print('{0} / {1}, {2}'.format(cnt, account_ids_len, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

            for match in match_json["matches"]:
                # print(str(match["game_id"]))
                f_game_ids.write(str(match["gameId"]) + "\n")

    # delete duplicate ids
    utility.delete_duplicated_records(utility.game_ids_file_path, True)


def get_game_info(first_ut, end_ut):
    with open(utility.game_ids_file_path) as f_game_ids:
        game_ids = f_game_ids.readlines()

    cnt = 0
    game_ids_len = len(game_ids)

    # print(datetime.date.fromtimestamp(first_ut / 1000).strftime("%m-%d-%y"))
    # print(datetime.date.fromtimestamp(end_ut / 1000).strftime("%m-%d-%y"))

    for game_id in game_ids:
        game_id = game_id.replace("\n", "")

        if os.path.exists(utility.game_info_directory_path + game_id + ".json"):
            print("[Already imported] skipped summonerId json = " + game_id)
            continue

        print("expected game_id json = " + game_id)
        game_info_json = utility.get_lol_game_info_json(utility.game_info_url, str(game_id))

        if game_info_json == "" or game_info_json == "429":
            print("skipped summonerId json = " + game_id)
            continue

        if not (first_ut <= game_info_json['gameCreation'] <= end_ut):
            print('skipped because refrain getting past data any more - info')
            return game_info_json['gameCreation']

        cnt += 1

        if cnt % 10 == 0:
            print('{0} / {1}, {2}'.format(cnt, game_ids_len, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

        print(utility.game_info_directory_path + game_id + ".json")

        with open(utility.game_info_directory_path + game_id + ".json", "w") as f_json:
            try:
                json.dump(game_info_json, f_json, separators=(',', ': '))
            except UnicodeEncodeError as e:
                print("UnicodeEncodeError [getMatchjson] game_id = " + game_id)
                # give up getting json

    return game_ids[-1]
"""
    with open(utility.game_ids_file_path) as f_game_ids:
        game_ids = f_game_ids.readlines()

    cnt = 0
    game_ids_len = len(game_ids)

    for game_id in game_ids:
        game_id = game_id.replace("\n", "")

        print("expected game_id json = " + game_id)
        game_info_json = utility.get_lol_game_info_json(utility.game_info_url, str(game_id))

        if game_info_json == "" or game_info_json == "429":
            print("skipped summonerId json = " + game_id)
            continue

        cnt += 1

        if cnt % 10 == 0:
            print(str(cnt) + " / " + str(game_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

        print(utility.game_info_directory_path + game_id + ".json")

        with open(utility.game_info_directory_path + game_id + ".json", "w") as f_json:
            try:
                json.dump(game_info_json, f_json, separators=(',', ': '))
            except UnicodeEncodeError as e:
                print("UnicodeEncodeError [getMatchjson] game_id = " + game_id)
                # give up getting json
"""


def get_game_timelines(last_game_id):
    with open(utility.game_ids_file_path) as f_game_ids:
        game_ids = f_game_ids.readlines()

    cnt = 0
    game_ids_len = len(game_ids)

    for game_id in game_ids:
        game_id = game_id.replace("\n", "")

        if not os.path.exists(utility.game_info_directory_path + game_id + ".json"):
            print('skipped because refrain getting past data any more - timeline')
            continue

        if os.path.exists(utility.game_timeline_directory_path + game_id + ".json"):
            print("[Already imported] skipped summonerId json = " + game_id)
            continue

        print("expected game_id json = " + game_id)
        timeline_json = utility.get_lol_game_timeline_json(utility.game_timeline_url, str(game_id))

        if timeline_json == "" or timeline_json == "429":
            print("skipped summonerId json = " + game_id)
            continue

        cnt += 1

        if cnt % 10 == 0:
            # print(str(cnt) + " / " + str(game_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            print('{0} / {1}, {2}'.format(cnt, game_ids_len, datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")))

        print(utility.game_timeline_directory_path + game_id + ".json")

        with open(utility.game_timeline_directory_path + game_id + ".json", "w") as f_json:
            try:
                json.dump(timeline_json, f_json, separators=(',', ': '))
            except UnicodeEncodeError as e:
                print("UnicodeEncodeError [getMatchjson] game_id = " + game_id)
                # give up getting json

        if last_game_id == game_id:
            return

if __name__ == "__main__":

    end_ut = math.floor(time.time()) * 1000

    # within 60 days
    first_ut = end_ut - (60 * 60 * 24 * 60 * 1000)

    # get_high_ranked_summoner_ids()
    # get_account_ids()

    print('fetching game ids')
    get_game_ids()
    last_game_id = get_game_info(first_ut, end_ut)
    get_game_timelines(last_game_id)