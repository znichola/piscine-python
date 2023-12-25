#!/bin/bash

script_path="$(dirname $(realpath $0))"
source $script_path/../.env

tables=(data_2022_dec data_2022_nov data_2022_oct data_2023_jan)

for table_name in "${tables[@]}"; do

echo "Create table ${table_name}"

docker exec -e PASSWORD=$POSTGRES_PASSWORD \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        -c "
CREATE TABLE ${table_name} (
    event_time TIMESTAMP NOT NULL,
    event_type VARCHAR(255) NOT NULL,
    product_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    user_id INTEGER NOT NULL,
    user_session VARCHAR(255)
);
"
done

for table_name in "${tables[@]}"; do

docker exec -e PASSWORD=mysecretpassword \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        --echo-all \
        -c "
COPY $table_name FROM '/subject/customer/${table_name}.csv' (FORMAT csv, HEADER);
"
done
