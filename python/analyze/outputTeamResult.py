# -*- coding: utf-8 -*-

import json
import collections
import os

matchResultFilePath = "../output/target/teamResult.csv"

fMatchResults = open(matchResultFilePath, 'w', encoding="UTF-8")

jsonFileNames = os.listdir('../output/game/')
decoder = json.JSONDecoder(object_pairs_hook=collections.OrderedDict)
filesCnt = len(jsonFileNames)
cnt = 0

for jsonFileName in jsonFileNames:
    f = open("../output/game/" + jsonFileName, "r")
    jsonData = decoder.decode(f.read())



    ## print json.dumps(jsonData, sort_keys = True, indent = 4)
    tmpArr = {}

    for participant in jsonData["participants"]:

        championId = str(participant["championId"])
        winFlg = participant["stats"]["winner"]
        lane = participant["timeline"]["lane"]
        participant["timeline"]["role"]

        if winFlg:
            if lane != "BOTTOM":
                tmpArr["WIN_" + lane] = championId
            else:
                role = participant["timeline"]["role"]

                if role == "DUO_CARRY":
                    tmpArr["WIN_ADC"] = championId
                else:
                    tmpArr["WIN_SUPPORT"] = championId
        else:
            if lane != "BOTTOM":
                tmpArr["LOSE_" + lane] = championId
            else:
                role = participant["timeline"]["role"]

                if role == "DUO_CARRY":
                    tmpArr["LOSE_ADC"] = championId
                else:
                    tmpArr["LOSE_SUPPORT"] = championId

##    for k, v in tmpArr.items():
##        print(k, v)

    if "WIN_TOP" in tmpArr and \
        "WIN_JUNGLE" in tmpArr and \
        "WIN_MIDDLE" in tmpArr and \
        "WIN_ADC" in tmpArr and \
        "WIN_SUPPORT" in tmpArr:

        winTeamRecord = "1," + \
                        tmpArr["WIN_TOP"] + "," + \
                        tmpArr["WIN_JUNGLE"] + "," + \
                        tmpArr["WIN_MIDDLE"] + "," + \
                        tmpArr["WIN_ADC"] + "," + \
                        tmpArr["WIN_SUPPORT"]

        fMatchResults.write(winTeamRecord + "\n")
        print(winTeamRecord)

    if "LOSE_TOP" in tmpArr and \
        "LOSE_JUNGLE" in tmpArr and \
        "LOSE_MIDDLE" in tmpArr and \
        "LOSE_ADC" in tmpArr and \
        "LOSE_SUPPORT" in tmpArr:

        loseTeamRecord = "0," + \
                        tmpArr["LOSE_TOP"] + "," + \
                        tmpArr["LOSE_JUNGLE"] + "," + \
                        tmpArr["LOSE_MIDDLE"] + "," + \
                        tmpArr["LOSE_ADC"] + "," + \
                        tmpArr["LOSE_SUPPORT"]

        fMatchResults.write(loseTeamRecord + "\n")
        print(loseTeamRecord)

    cnt += 1

    if cnt % 100 == 0:
        print(cnt, filesCnt)

fMatchResults.close()

"""
    print(str(participant["championId"]) + "," +
              participant["timeline"]["lane"] + "," +
              participant["timeline"]["role"] + "," + str(int(participant["stats"]["winner"])))
"""
##    print(participant["stats"]["winner"])

f.close()
