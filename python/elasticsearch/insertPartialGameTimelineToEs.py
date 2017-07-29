import sys
sys.path.append("../collectInformation")
import utility

import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Test") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

sc = spark.sparkContext

path = utility.game_info_directory_path + "*.json"
matchDf = spark.read.json(path)


matchRdd = matchDf.rdd

team1 = matchRdd.map(lambda x: (x["teams"][0][12], x["teams"][0][15], x["teams"][0][11]))
team2 = matchRdd.map(lambda x: (x["teams"][1][12], x["teams"][1][15], x["teams"][1][11]))

teams = team1.union(team2)

tmp = teams.toDF(['team', 'winner', 'riftHeraldKills']) \
    .groupBy("winner", "riftHeraldKills") \
    .count()
print(tmp.show())
