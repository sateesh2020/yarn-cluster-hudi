## Build Yarn Images
cd yarn

docker build -f Dockerfile-base -t hadoop-base:3.3.6 .

docker build -f Dockerfile-spark -t hadoop-spark-base:3.3.6 .

cd ..

## Build Hive Images
cd hive

cd base
docker build -t hadoop-hive-base:3.3.6 .

cd ..

cd metastore-pg
docker build -t metastore-postgres:11 .

cd ..

cd ..

## Build Trino
cd trino 

cd ./base
docker build -t trino-base:368 .
cd ..

cd ./trino-worker
docker build -t trino-worker:368 .
cd ..

cd ./trino-coordinator
docker build -t trino-coordinator:368 .
cd ..

cd ..