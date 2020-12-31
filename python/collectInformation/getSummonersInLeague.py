import utility

# Output Master and Challenger summoner ids to a files
# 1. summonerChallenger.csv
# 2. summonerMaster.csv
#
# Then, They are combined to a file, summoners.csv with no duplicated ids

final_page = 100
tier = "IRON"
divisions = [1, 2, 3, 4]
summoner_auto_number = 1

# with open(utility.general_summoners_file_path, 'w', encoding="UTF-8") as f_summoners:
with open(utility.general_summoners_file_path, 'w', encoding="UTF-8") as f_summoners:
    f_summoners.write('id,tier,division,summonerId,summonerName,leaguePoints,win,lose,total,veteran,inactive,freshBlood,hotStreak\n')

    for division in divisions:
        for page in range(1, final_page + 1):
            summoners_json = utility.get_lol_summoners_in_league_json(division, tier, page)

            if not summoners_json:
                break

            for summoner in summoners_json:
                f_summoners.write(u"{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}\n".format(
                    summoner_auto_number, tier, division,
                    summoner['summonerId'], summoner['summonerName'], summoner['leaguePoints'],
                    summoner['wins'], summoner['losses'], summoner['wins'] + summoner['losses'],
                    summoner['veteran'] + 0, summoner['inactive'] + 0, summoner['freshBlood'] + 0,
                    summoner['hotStreak'] + 0
                ))

                summoner_auto_number += 1


# make unique summoner ids in a file
# utility.delete_duplicated_records(utility.summoners_file_path, False)


