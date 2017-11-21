
import utility
from datetime import datetime
import json


def get_high_ranked_summoner_ids():
    # Output Master and Challenger summoner ids to a files
    # 1. summonerChallenger.csv
    # 2. summonerMaster.csv
    #
    # Then, They are combined to a file, summoners.csv with no duplicated ids

    challenger_summoner_json = utility.get_lol_challenger_summoners_id_json()
    master_summoner_json = utility.get_lol_master_summoners_id_json()

    # output challenger ids
    with open(utility.summoners_file_path, 'w', encoding="UTF-8") as f_summoners:
        if challenger_summoner_json != "":
            with open(utility.challenger_summoners_file_path, 'w', encoding="UTF-8") as f_challengers:
                for summoner in challenger_summoner_json["entries"]:
                    f_challengers.write(summoner["playerOrTeamId"] + "\n")
                    f_summoners.write(summoner["playerOrTeamId"] + "\n")

    # output master ids
    with open(utility.summoners_file_path, 'w', encoding="UTF-8") as f_summoners:
        if master_summoner_json != "":
            with open(utility.master_summoners_file_path, 'w', encoding="UTF-8") as f_masters:
                for summoner in master_summoner_json["entries"]:
                    f_masters.write(summoner["playerOrTeamId"] + "\n")
                    f_summoners.write(summoner["playerOrTeamId"] + "\n")

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
                print(accountJson["accountId"])

            cnt += 1

            if cnt % 10 == 0:
                print(str(cnt) + " / " + str(summonerIdsLen) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))


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
                print(str(cnt) + " / " + str(account_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

            for match in match_json["matches"]:
                # print(str(match["game_id"]))
                f_game_ids.write(str(match["gameId"]) + "\n")

    # delete duplicate ids
    utility.delete_duplicated_records(utility.game_ids_file_path, False)


def get_game_info_json():
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


def get_game_timeline_json():
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
                print(str(cnt) + " / " + str(account_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

            for match in match_json["matches"]:
                # print(str(match["game_id"]))
                f_game_ids.write(str(match["gameId"]) + "\n")

    # delete duplicate ids
    utility.delete_duplicated_records(utility.game_ids_file_path, False)


    with open(utility.game_ids_file_path) as f_game_ids:
        game_ids = f_game_ids.readlines()

        cnt = 0
        game_ids_len = len(game_ids)

        for game_id in game_ids:
            game_id = game_id.replace("\n", "")

            print("expected game_id json = " + game_id)
            timeline_json = utility.get_lol_game_timeline_json(utility.game_timeline_url, str(game_id))

            if timeline_json == "" or timeline_json == "429":
                print("skipped summonerId json = " + game_id)
                continue

            cnt += 1

            if cnt % 10 == 0:
                print(str(cnt) + " / " + str(game_ids_len) + " " + datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

            print(utility.game_timeline_directory_path + game_id + ".json")

            with open(utility.game_timeline_directory_path + game_id + ".json", "w") as f_json:
                try:
                    json.dump(timeline_json, f_json, separators=(',', ': '))
                except UnicodeEncodeError as e:
                    print("UnicodeEncodeError [getMatchjson] game_id = " + game_id)
                    # give up getting json