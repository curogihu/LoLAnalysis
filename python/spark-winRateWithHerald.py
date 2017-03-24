import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Test") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext
path = "../output/game/*.json"
matchDf = spark.read.json(path)

# tmp = sc.parallelize(matchDf)
# tmp = matchDf.map(lambda x: x["matchId"])
# print(tmp.first())

matchRdd = matchDf.rdd
# ok
# [12] = teamId, [15] = winner, [11] = riftHeraldKills, [3] = c, [1] = baronKills

# teams1 = matchRdd.map(lambda x: (x["teams"][0][12], x["teams"][0][15], x["teams"][0][11], x["teams"][0][3], x["teams"][0][1])).collect()
# teams2 = matchRdd.map(lambda x: (x["teams"][1][12], x["teams"][1][15], x["teams"][1][11], x["teams"][1][3], x["teams"][1][1])).collect()

# team1 = matchRdd.map(lambda x: (x["teams"][0][12], x["teams"][0][15], x["teams"][0][11], x["teams"][0][3], x["teams"][0][1]))
# team2 = matchRdd.map(lambda x: (x["teams"][1][12], x["teams"][1][15], x["teams"][1][11], x["teams"][1][3], x["teams"][1][1]))

team1 = matchRdd.map(lambda x: (x["teams"][0][12], x["teams"][0][15], x["teams"][0][11]))
team2 = matchRdd.map(lambda x: (x["teams"][1][12], x["teams"][1][15], x["teams"][1][11]))

# teams = team1.union(team2).collect()
teams = team1.union(team2)

tmp = teams.toDF(['team', 'winner', 'riftHeraldKills'])\
            .groupBy("winner", "riftHeraldKills")\
            .count()
print(tmp.show())
# result = teams.map(lambda x: (str(x[1]) + "-" + str(x[2]), 1))

# resultCounts = result.reduceByKey(lambda x, y: x + y).collect()

# for tmp in result:
#    print(tmp)

# df = teams.toDF(['team', 'winner', 'riftHeraldKills', 'dragonKills', 'baronKills'])

# print(df)
#res = df.stat.crosstab('winner','riftHeraldKills')
# print(res.show())
# print(df.show(10))



# herald = teams.map(lambda x: True if x[2] == 1 else False)
# heraldCnt = teams.filter(lambda x: (x[0], 1) if x[2] == 1 else (x[0], 0))

# I had not touch what i prgoram

#   print(heraldCnt)

# noHerald = teams.map(lambda x: True if x[2] == 0 else False)

# timelines = matchRdd.map(lambda x: x["timeline"]).collect()
# timelines = matchRdd.map(lambda x: x["timeline"][1][2]["events"]).collect()

# print(type(matchRdd))
# print(matchRdd.first())

# ok

# for team in team1:
#    print(team)

# for team in team2:
#    print(team)


# for team in teams:
#     print(team)



"""
for team in herald:
    print(team)
"""

"""
# for timeline in timelines:
#    for event in timeline:
#        print(event)

#    print("----------------------------------")
#    print(timeline)

# ok


matchDf.createOrReplaceTempView("master")

matchIdDf = spark.sql("SELECT distinct matchId FROM master")
print(matchIdDf.show())



df = spark.read.json("../output/game/7.4-test/*.json")


ng
jsonRdd = df.map(lambda x: x[2])
print(df.show())


print(df.printSchema())

# print(df.show())

+---------+-----+
|matchMode|count|
+---------+-----+
|     ARAM|   99|
|      URF| 1532|
|  CLASSIC| 6449|
+---------+-----+
countsByMatchMode = df.groupBy("matchMode").count()
print(countsByMatchMode.show())
"""

# print(df["participantIdentities"])