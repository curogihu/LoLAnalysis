from datetime import datetime

import utility

# account_ids = open("../output/list/accounts.csv").readlines()

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