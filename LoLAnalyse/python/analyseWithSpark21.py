import findspark
findspark.init()

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Test") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.json("../output/game/*.json")

# print(df.show())
countsByMatchMode = df.groupBy("matchMode").count()

print(countsByMatchMode.show())

# print(df["participantIdentities"])