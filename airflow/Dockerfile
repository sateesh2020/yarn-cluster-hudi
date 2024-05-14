FROM apache/airflow:2.7.1-python3.11

USER root
RUN apt-get update && \
    apt-get install -y gcc python3-dev openjdk-11-jdk procps wget iputils-ping && \
    apt-get clean

ARG SPARK_VERSION=3.4.2
ARG HADOOP_VERSION=3.3.6

# Set JAVA_HOME environment variable
ENV JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64"
#RUN chmod 777 /usr/lib/jvm/java-11-openjdk-amd64/

ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}

RUN mkdir -p ${HADOOP_HOME} && mkdir -p ${SPARK_HOME}
WORKDIR ${SPARK_HOME}

# Download and install Spark
RUN curl https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz -o spark-${SPARK_VERSION}-bin-hadoop3.tgz \
 && tar xvzf spark-${SPARK_VERSION}-bin-hadoop3.tgz --directory /opt/spark --strip-components 1 \
 && rm -rf spark-${SPARK_VERSION}-bin-hadoop3.tgz

# Download and install Hadoop
RUN curl https://dlcdn.apache.org/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz -o hadoop-${HADOOP_VERSION}-bin.tar.gz \
 && tar xfz hadoop-${HADOOP_VERSION}-bin.tar.gz --directory /opt/hadoop --strip-components 1 \
 && rm -rf hadoop-${HADOOP_VERSION}-bin.tar.gz

# Add the Spark and Hadoop bin and sbin to the PATH variable.
# Also add $JAVA_HOME/bin to the PATH
ENV PATH="$SPARK_HOME/sbin:/opt/spark/bin:${PATH}"
ENV PATH="$HADOOP_HOME/bin:$HADOOP_HOME/sbin:${PATH}"
ENV PATH="${PATH}:${JAVA_HOME}/bin"

# Setup environment variables
ENV PYSPARK_PYTHON python3
ENV HADOOP_CONF_DIR="$HADOOP_HOME/etc/hadoop"

# Add Hadoop native library path to the dynamic link library path
ENV LD_LIBRARY_PATH="$HADOOP_HOME/lib/native:${LD_LIBRARY_PATH}"

# Set user for HDFS and Yarn (for production probably not smart to put root)
ENV HDFS_NAMENODE_USER="root"
ENV HDFS_DATANODE_USER="root"
ENV HDFS_SECONDARYNAMENODE_USER="root"
ENV YARN_RESOURCEMANAGER_USER="root"
ENV YARN_NODEMANAGER_USER="root"

# Add JAVA_HOME to haddop-env.sh
RUN echo "export JAVA_HOME=${JAVA_HOME}" >> "$HADOOP_HOME/etc/hadoop/hadoop-env.sh"

# COPY the appropriate configuration files to their appropriate locations
# COPY conf/spark-defaults.conf "$SPARK_HOME/conf/"
COPY conf/*.xml "$HADOOP_HOME/etc/hadoop/"

# Make the binaries and scripts executable and set the PYTHONPATH environment variable
RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*

ENV PYTHONPATH=$SPARK_HOME/python/:$PYTHONPATH
#ENV PYTHONPATH=$SPARK_HOME/python/lib/py4j-0.10.9.5-src.zip:$PYTHONPATH

# RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
#   cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
#   chmod 600 ~/.ssh/authorized_keys

# COPY ssh_config ~/.ssh/config

USER airflow 

RUN pip install apache-airflow apache-airflow-providers-apache-spark dbt-core dbt-postgres dbt-spark[PyHive] dbt-core airflow-dbt
USER root
RUN mkdir -p -m 777 /opt/airflow/dbt
RUN mkdir -p -m 777 /opt/airflow/logs
# RUN chmod a+x /usr/bin/git
RUN chmod 777 /opt/airflow/dbt