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

DELETE FROM temp_customers a
WHERE a.ctid <> (SELECT min(b.ctid)
                 FROM   temp_customers b
                 WHERE  a.event_time = b.event_time AND
						a.event_type = b.event_type AND
						a.product_id = b.product_id AND
						a.price = b.price AND
						a.user_id = b.user_id AND
						a.user_session = b.user_session AND);
"



# SELECT * FROM customers 
# GROUP BY user_id, event_type, event_time, product_id, price, user_session
# HAVING COUNT(*)>1 LIMIT 100;

# SELECT DISTINCT user_id, event_type, event_time, product_id, price, user_session
# FROM customers
# LIMIT 100;

# CREATE TEMP TABLE temp_data AS
# SELECT * FROM customers;

# SELECT 16536158
# Query returned successfully in 24 secs 995 msec.
