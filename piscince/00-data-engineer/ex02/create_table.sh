#!/bin/bash

cat ../subject/customer/data_2022_oct.csv | \
    docker exec -e PASSWORD=mysecretpassword \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        -c "COPY data_2022_oct FROM STDIN WITH CSV;"

# line that worked in psql form local file
# \copy data_2022_oct FROM /home/data_2022_oct.csv WITH (FORMAT csv);
