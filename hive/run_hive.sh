#!/bin/bash

cd ./base
docker build -t hadoop-hive-base:3.1.3 .
cd ..

cd ./metastore-pg
docker build -t metastore-postgres:11 .
cd ..

docker compose up -d
