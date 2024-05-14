#!/bin/bash

cd ./base
docker build -t trino-base:368 .
cd ..

docker compose up -d
