#!/bin/bash

SPARK_WORKLOAD=$1

echo "SPARK_WORKLOAD: $SPARK_WORKLOAD"

/etc/init.d/ssh start

if [ "$SPARK_WORKLOAD" == "master" ];
then
  hdfs namenode -format

  # start the master node processes
  hdfs --daemon start namenode
  #hdfs --daemon start secondarynamenode
  yarn --daemon start resourcemanager

  # create required directories
  while ! hdfs dfs -mkdir -p /spark-logs;
  do
    echo "Failed creating /spark-logs hdfs dir"
  done
  echo "Created /spark-logs hdfs dir"
  hdfs dfs -mkdir -p /opt/spark/data
  echo "Created /opt/spark/data hdfs dir"


  # copy the data to the data HDFS directory
  hdfs dfs -copyFromLocal /opt/spark/data/* /opt/spark/data
  hdfs dfs -ls /opt/spark/data

  if ! hdfs dfs -test -d "$SPARK_JARS_HDFS_PATH"
  then
    echo "Formatting directory: $SPARK_JARS_HDFS_PATH"
    hdfs dfs -mkdir -p  "$SPARK_JARS_HDFS_PATH"
    hdfs dfs -put "$SPARK_HOME"/jars/* "$SPARK_JARS_HDFS_PATH"/
    hdfs dfs -put /opt/jars "$SPARK_JARS_HDFS_PATH"/
  fi

elif [ "$SPARK_WORKLOAD" == "worker" ];
then
  hdfs namenode -format

  # start the worker node processes
  hdfs --daemon start datanode
  yarn --daemon start nodemanager
elif [ "$SPARK_WORKLOAD" == "adhoc" ];
then
  # Start Thrift Server
  # start-thriftserver.sh --hiveconf hive.server2.thrift.port 10000 --hiveconf hive.server2.authentication NOSASL
  while ! hdfs dfs -test -d /spark-logs;
  do
    echo "spark-logs doesn't exist yet... retrying"
    sleep 1;
  done
  echo "Exit loop"

  # start the spark history server
  start-history-server.sh
  #notebook
fi

tail -f /dev/null
