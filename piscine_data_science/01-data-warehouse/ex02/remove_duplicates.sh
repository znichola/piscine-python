#!/bin/bash

script_path="$(dirname $(realpath $0))"
source $script_path/../.env

echo "Removing dublicates"

docker exec -e PASSWORD=$POSTGRES_PASSWORD \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        -c "

"

# SELECT * FROM customers 
# GROUP BY user_id, event_type, event_time, product_id, price, user_session
# HAVING COUNT(*)>1 LIMIT 100;
