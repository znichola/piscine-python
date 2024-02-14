#!/bin/bash

# hack to get it to work on the macs
realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

script_path="$(dirname $(realpath $0))"
source $script_path/../.env

# Add Customer data
customer_data=($(ls ../subject/customer | cut -f 1 -d '.' -))

for table_name in "${customer_data[@]}"; do

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
COPY $table_name FROM '/subject/customer/${table_name}.csv' (FORMAT csv, HEADER);
"
done

