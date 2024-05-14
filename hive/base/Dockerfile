# builder step used to download and configure spark environment
FROM hadoop-spark-base:3.3.6 AS builder

COPY run_hive_global_commit_tool.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run_hive_global_commit_tool.sh

COPY run_sync_tool.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/run_sync_tool.sh

COPY startup.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/startup.sh

# NOTE: This is the only battle-proven method to inject jars into Hive CLI
ENV AUX_CLASSPATH=file://${HUDI_HADOOP_BUNDLE}

RUN rm -rf $HIVE_HOME/lib/guava*.jar
RUN cp $HADOOP_HOME/share/hadoop/common/lib/guava-*.jar $HIVE_HOME/lib/
#RUN mv $HIVE_HOME/lib/log4j-slf4j-impl-2.10.0.jar $HIVE_HOME/lib/log4j-slf4j-impl-2.10.0.jar.bak

EXPOSE 10000
EXPOSE 10001
EXPOSE 10002
EXPOSE 9083

CMD startup.sh