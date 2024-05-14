#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
# Trino docker setup is adapted from https://github.com/Lewuathe/docker-trino-cluster
# trino-coordinator  | ERROR: Trino requires Java 11+ (found 1.8.0_212)
# trino-coordinator exited with code 100
# trino-worker       | ERROR: Trino requires Java 11+ (found 1.8.0_212)
# trino-worker exited with code 100
FROM openjdk:11-jdk-slim-bullseye as jdk
FROM hadoop-base:3.3.6 as hadoop-base

ENV TRINO_VERSION=368
ENV TRINO_HOME=/usr/local/trino
ENV BASE_URL=https://repo1.maven.org/maven2

RUN apt-get update
RUN apt-get install -y \
    curl \
    tar \
    sudo \
    rsync \
    wget \
    python3-pip \
    build-essential \
    uuid-runtime \
    less

COPY --from=jdk /usr/local/openjdk-11 /usr/lib/jvm/java-11-openjdk-arm64/
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64
ENV PATH $PATH:$JAVA_HOME/bin

RUN rm -rf /usr/lib/jvm/java-8-openjdk-arm64

WORKDIR /usr/local/bin
RUN wget -q ${BASE_URL}/io/trino/trino-cli/${TRINO_VERSION}/trino-cli-${TRINO_VERSION}-executable.jar
RUN chmod +x trino-cli-${TRINO_VERSION}-executable.jar
RUN mv trino-cli-${TRINO_VERSION}-executable.jar trino-cli

WORKDIR /usr/local
RUN wget -q ${BASE_URL}/io/trino/trino-server/${TRINO_VERSION}/trino-server-${TRINO_VERSION}.tar.gz
RUN tar xvzf trino-server-${TRINO_VERSION}.tar.gz -C /usr/local/
RUN ln -s /usr/local/trino-server-${TRINO_VERSION} $TRINO_HOME
RUN rm trino-server-${TRINO_VERSION}.tar.gz

ENV TRINO_BASE_WS /opt
RUN mkdir -p ${TRINO_BASE_WS}/target/
RUN wget -O ${TRINO_BASE_WS}/target/hudi-trino-bundle.jar "https://github.com/sateesh2020/hudi-jars/releases/download/hudi-0.14.1/hudi-trino-bundle-0.14.1.jar"

#COPY hudi-trino-bundle-0.14.1.jar ${TRINO_BASE_WS}/target/hudi-trino-bundle.jar

ENV HUDI_TRINO_BUNDLE ${TRINO_BASE_WS}/target/hudi-trino-bundle.jar
RUN cp ${HUDI_TRINO_BUNDLE} ${TRINO_HOME}/plugin/hive/

ADD scripts ${TRINO_HOME}/scripts
RUN chmod +x ${TRINO_HOME}/scripts/trino.sh

RUN mkdir -p $TRINO_HOME/data
VOLUME ["$TRINO_HOME/data"]
