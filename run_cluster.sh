#!/bin/bash
#!/bin/bash
# exit when any command fails
set -e
# trace the bash script command that is being executed
set -o xtrace

# expand alias
#docker login
shopt -s expand_aliases
# create new network
docker network create hadoop_network || true

#export COMPOSE_PROJECT_NAME=prod

while getopts s: flag
do
        case "${flag}" in
                s) servicename=${OPTARG};;
        esac
done

if [ -z "$servicename" ]
then
        echo "Missing Servicename arguement : -servicename "
        exit 1
fi

if [ $servicename = "yarn" ]; then
echo "Deploying namenode resourcemanager spark-historyserver"
cd yarn
docker compose  -f docker-compose.yml up -d
cd ..

elif  [ $servicename = "hive" ]; then
echo "Deploying metastore-postgresql hiveserver"
cd hive
docker compose  -f docker-compose.yml up -d
cd ..

elif  [ $servicename = "trino" ]; then
echo "Deploying trino-worker trino-coordinator"
cd trino
docker compose  -f docker-compose.yml up -d
cd ..
else
echo "No service"
fi