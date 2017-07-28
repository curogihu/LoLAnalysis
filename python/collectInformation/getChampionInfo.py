import utility

champions_json = utility.get_lol_game_champion_info_json()

if champions_json:
    with open(utility.champions_file_path, 'w', encoding="UTF-8") as f_champions:
        champion_data = champions_json["data"]

        for champion_info in champion_data.values():
            f_champions.write(str(champion_info["id"]) + "," +
                                    champion_info["key"] + "," +
                                    champion_info["name"] + "\n")
