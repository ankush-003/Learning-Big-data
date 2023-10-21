#!/usr/bin/env python3

# imports
import sys
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Learning Spark") \
    .getOrCreate()

print(spark)

def readData(file: str):
    df = spark.read \
            .option("InferSchema","true") \
            .option("header","true") \
            .csv(file)
    # df.show(n=5)        
    # df.printSchema()
    return df

df12, df13, df14 = readData(sys.argv[1]), readData(sys.argv[2]), readData(sys.argv[3])
df = df12.unionByName(df13)
df = df.unionByName(df14)
df = df.groupBy("state_code").count()
# df.show()

state_keys = readData(sys.argv[4]).select(['state_code', 'state_name']).distinct()
# state_keys.show()

top_states = df.join(state_keys, 'state_code','inner')\
        .orderBy('count',ascending=0)\
        .select('state_name')\
        .limit(10)

top_states_list = top_states.rdd.flatMap(lambda x: x).collect()

print(top_states_list)

