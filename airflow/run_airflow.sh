#!/bin/bash

docker build -t airflow-hadoop-base:2.7.1 .

docker compose up -d