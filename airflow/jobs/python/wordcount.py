from pyspark.sql import SparkSession
import socket

try:
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    spark = (
        SparkSession.builder.appName("PythonWordCount")
        .config("spark.driver.memory", "2")
        .config("spark.executor.memory", "2")
        .master("local[*]")
        .getOrCreate()
    )
    text = "Hello Spark Hello Python Hello Airflow Hello Docker and Hello Yusuf"

    words = spark.sparkContext.parallelize(text.split(" "))

    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    print(wordCounts)
    for wc in wordCounts.collect():
        print(wc[0], wc[1])

    spark.stop()
except Exception as e:
    print("Error running Job:", e)
    spark.stop()
