import findspark
findspark.init()

import os
from pyspark.sql import SparkSession

input_champions_file_path = os.path.join("C:", os.sep, "output", "edit", "static-data", "champions.csv")
input_info_file_path = os.path.join("C:", os.sep, "output", "edit", "info", "info_per_line.csv")


def loadChampionNames():
    championNames = {}
    with open(input_champions_file_path) as f:
        next(f)     # skip the header

        for line in f:
            fields = line.split(',')

            # print(type(fields[0]), fields[0])
            # print(type(fields[2]), fields[2])

            championNames[int(fields[0])] = fields[2]
    return championNames

spark = SparkSession.builder.appName("SimpleApp").getOrCreate()
lines = spark.read.option("header", "true") \
                    .option("delimiter", ",") \
                    .option("inferSchema", "true") \
                    .text(input_info_file_path)


# lines = spark.read.format("csv").option("header", "true").load(input_info_file_path)

# lines = sc.textFile(input_info_file_path)
# header = lines.first() #extract header
# lines = lines.filter(row: row != header)   #filter out header
"""
results = sc.textFile(input_info_file_path) \
            .map(lambda line: line.split(","), 1) \
            .filter(lambda line: len(line) <= 1) \
            .collect()
"""
"""
results = sc.read.format("com.databricks.spark.csv") \
                .option("header", "true") \
                .option("inferschema", "true") \
                .option("mode", "DROPMALFORMED") \
                .load(input_info_file_path)

for result in results:
    print(result)
"""
"""
# champions = lines.map(lambda x: (int(x.split(",")[2]), 1))
championCounts = champions.reduceByKey(lambda x, y: x + y)

flipped = championCounts.map(lambda x: (x[1], x[0]))
sortedChampions = flipped.sortByKey()

sortedChampionsWithNames = sortedChampions.map(lambda countChampion : (nameDict.value[countChampion[1]], countChampion[0]))

print(loadChampionNames())

results = sortedChampionsWithNames.collect()

for result in results:
    print(result)
"""