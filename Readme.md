## Build Images

```shell
./build_images.sh
```

## Running Services

### Yarn with Spark on Hadoop

More details on the [Yarn](yarn/Readme.md) page.

```shell
cd yarn
docker compose up --build -d

```

### Hive Server

More details on the [Hive](hive/Readme.md) page.

```shell
cd hive
docker compose up --build -d
```

### Trino

More details on the [Trino](trino/Readme.md) page.

```shell
cd trino
docker compose up --build -d
```
