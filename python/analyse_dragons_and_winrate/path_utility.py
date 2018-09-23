import os
import glob

# in case of Windows
if os.name == "nt":
    json_files_path = glob.glob(os.path.join("C:", os.sep, "output", "game", "info", "*.json"))
    win_team_log_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "win_team_log.csv")

    input_killed_log_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "killed_log.csv")
    input_win_team_log_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "win_team_log.csv")
    output_merged_file_path = os.path.join("C:", os.sep, "output", "edit", "boss_killed_log", "merged_two_logs.csv")

# in case of linux and Mac
elif os.name == "posix":
    json_files_path = glob.glob(os.path.join("", os.sep, "Applications", "output", "game", "info", "*.json"))
    win_team_log_path = os.path.join("", os.sep, "Applications", "output", "edit", "boss_killed_log", "win_team_log.csv")

    input_killed_log_file_path = os.path.join("", os.sep, "Applications", "output", "edit", "boss_killed_log", "killed_log.csv")
    input_win_team_log_file_path = os.path.join("", os.sep, "Applications", "output", "edit", "boss_killed_log", "win_team_log.csv")
    output_merged_file_path = os.path.join("", os.sep, "Applications", "output", "edit", "boss_killed_log", "merged_two_logs.csv")
