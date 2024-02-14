#!/bin/bash

# hack to get it to work on the macs
realpath() {
    [[ $1 = /* ]] && echo "$1" || echo "$PWD/${1#./}"
}

script_path="$(dirname $(realpath $0))"
source $script_path/../.env

echo "Create table item"

docker exec -e PASSWORD=$POSTGRES_PASSWORD \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        -c "
CREATE TABLE item (
    product_id INTEGER NOT NULL,
    category_id BIGINT,
    category_code VARCHAR(255),
    brand VARCHAR(255)
);
COPY item FROM '/subject/item/item.csv' (FORMAT csv, HEADER);
"