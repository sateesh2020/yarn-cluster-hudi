from pyspark.sql import SparkSession
import socket

# Configure Spark application
# spark = SparkSession.builder \
#     .appName("Hudi Streamer - Active Customers") \
#     .config("spark.jars.packages", "org.apache.hudi:hudi-spark3.3-bundle_2.12:0.14.1") \
#     .config("spark.jars.packages", "org.apache.hudi:hudi-utilities_2.12:0.14.1") \
#     .config("spark.executor.memory", "4g") \
#     .config("spark.driver.memory", "2g") \
#     .config("spark.executors", 4) \
#     .config("spark.sql.hive.warehouse.dir", "/user/hive/warehouse") \
#     .getOrCreate()

spark = (
    SparkSession.builder.appName("Python Test")
    .config("spark.executor.memory", "4g")
    .config("spark.driver.memory", "2g")
    .config("spark.executors", 4)
    .getOrCreate()
)

# Set Hudi configuration (assuming you have a way to access HUDI_UTILITIES_BUNDLE)
# hoodie_conf = {
#     "hoodie.datasource.hive_sync.jdbcurl": "jdbc:hive2://172.20.4.53:10000",
#     "hoodie.table.type": "COPY_ON_WRITE"
# }

# # Set source and target details
# source_class = "org.apache.hudi.utilities.sources.JdbcSource"
# source_ordering_field = "id"
# target_base_path = "/user/hive/warehouse/customers"
# target_table = "customers"

# # Load properties from file (assuming you can read from /user/jdbc-ingestion.properties)
# with open("/opt/airflow/config/jdbc-ingestion.properties", "r") as f:
#     props = f.read().strip()  # Read and remove trailing whitespace

# # Define schema provider class
# schemaprovider_class = "org.apache.hudi.utilities.schema.JdbcbasedSchemaProvider"

# HUDI_UTILITIES_BUNDLE = '/var/hoodie/ws/docker/hoodie/hadoop/hive_base/target/hoodie-utilities.jar'

sc = spark.sparkContext

# (Assuming you have access to the necessary Hudi classes)
try:
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)
    # Use Hudi streamer class (replace with appropriate import if needed)
    # from org.apache.hudi.utilities.streamer import HoodieStreamer

    # Create Hudi streamer instance
    #   streamer = sc._jvm.org.apache.hudi.utilities.streamer.HoodieStreamer(hoodie_conf, spark)

    #   # Configure streamer with options
    #   #streamer.set_jars("/opt/postgresql-42.5.0.jar")
    #   #streamer.set_hoodie_conf(hoodie_conf)
    #   streamer.set_source_class(source_class)
    #   streamer.set_source_ordering_field(source_ordering_field)
    #   streamer.set_target_base_path(target_base_path)
    #   streamer.set_target_table(target_table)
    #   streamer.set_props(props)
    #   streamer.set_schemaprovider_class(schemaprovider_class)
    #   streamer.set_enable_hive_sync(True)

    #   # Start streaming data
    #   streamer.run(HUDI_UTILITIES_BUNDLE)  # Assuming you have HUDI_UTILITIES_BUNDLE defined

    # Stop Spark session
    # spark.stop()
    text = "Hello Spark Hello Python Hello Airflow Hello Docker and Hello Yusuf"

    words = spark.sparkContext.parallelize(text.split(" "))

    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

    print(wordCounts)
    for wc in wordCounts.collect():
        print(wc[0], wc[1])

except Exception as e:
    print("Error running Job:", e)
    # spark.stop()
