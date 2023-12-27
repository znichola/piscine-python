#!/bin/bash

script_path="$(dirname $(realpath $0))"
source $script_path/../.env

echo "Create merged customer table"

tables=($(docker exec -e PASSWORD=$POSTGRES_PASSWORD \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        --tuples-only \
        -c "
    SELECT tablename FROM pg_tables
        WHERE schemaname='public'
        AND tablename LIKE 'data_202%';
"))


docker exec -e PASSWORD=$POSTGRES_PASSWORD \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        --tuples-only \
        -c "
    CREATE TABLE IF NOT EXISTS customers (
        event_time TIMESTAMP NOT NULL,
        event_type VARCHAR(255) NOT NULL,
        product_id INTEGER NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        user_id INTEGER NOT NULL,
        user_session VARCHAR(255)
    );
"

for table_name in "${tables[@]}"; do

echo "Inserting ${table_name}"

docker exec -e PASSWORD=$POSTGRES_PASSWORD \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        -c "
    INSERT INTO customers SELECT * FROM ${table_name}
"
done