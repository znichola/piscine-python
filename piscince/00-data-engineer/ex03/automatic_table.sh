#!/bin/bash

script_path="$(dirname $(realpath $0))"
source $script_path/../.env

# Add Customer data
customer_data=($(ls ../subject/customer | cut -f 1 -d '.' -))

# for table_name in "${customer_data[@]}"; do

# echo "Create table ${table_name}"

# docker exec -e PASSWORD=$POSTGRES_PASSWORD \
#     postgres psql \
#         -U znichola \
#         -d piscineds \
#         -h localhost \
#         -c "
# CREATE TABLE ${table_name} (
#     event_time TIMESTAMP NOT NULL,
#     event_type VARCHAR(255) NOT NULL,
#     product_id INTEGER NOT NULL,
#     price DECIMAL(10, 2) NOT NULL,
#     user_id INTEGER NOT NULL,
#     user_session VARCHAR(255)
# );
# COPY $table_name FROM '/subject/customer/${table_name}.csv' (FORMAT csv, HEADER);
# "
# done

# Add Items data
item_data=($(ls ../subject/item | cut -f 1 -d '.' -))

for table_name in "${item_data[@]}"; do

echo "Create table ${table_name}"

# product_id,category_id,category_code,brand

docker exec -e PASSWORD=$POSTGRES_PASSWORD \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        -c "
CREATE TABLE ${table_name} (
    product_id INTEGER NOT NULL,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255)
);
COPY $table_name FROM '/subject/item/${table_name}.csv' (FORMAT csv, HEADER);
"
done
