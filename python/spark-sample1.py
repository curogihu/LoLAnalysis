import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Test") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext
path = "../output/game/7.4-test/*.json"
matchDf = spark.read.json(path)

# tmp = sc.parallelize(matchDf)
# tmp = matchDf.map(lambda x: x["matchId"])
# print(tmp.first())

matchRdd = matchDf.rdd
# ok
# [12] = teamId, [15] = winner, [11] = riftHeraldKills, [3] = dragonKills, [1] = baronKills
teams1 = matchRdd.map(lambda x: (x["teams"][0][12], x["teams"][0][15], x["teams"][0][11], x["teams"][0][3], x["teams"][0][1])).collect()
teams2 = matchRdd.map(lambda x: (x["teams"][1][12], x["teams"][1][15], x["teams"][1][11], x["teams"][1][3], x["teams"][1][1])).collect()

timelines = matchRdd.map(lambda x: x["timeline"][1][2]["events"]).collect()

# print(type(matchRdd))
# print(matchRdd.first())

"""
# ok
for team in teams1:
    print(team)

for team in teams2:
    print(team)
"""

for timeline in timelines:
    for event in timeline:
        print(event)

    print("----------------------------------")
    # print(timeline)

# ok

for tmp in test:
    print(tmp)
    print("----------------------------------")



"""
matchDf.createOrReplaceTempView("master")

matchIdDf = spark.sql("SELECT distinct matchId FROM master")
print(matchIdDf.show())
"""

"""
df = spark.read.json("../output/game/7.4/*.json")


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