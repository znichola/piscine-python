#!/bin/bash

head ../subject/customer/data_2022_oct.csv | \
    docker exec postgres /bin/cat

echo test two

cat ../subject/customer/data_2022_oct.csv | \
    docker exec -e PASSWORD=mysecretpassword \
    postgres psql \
        -U znichola \
        -d piscineds \
        -h localhost \
        --echo-all \
        -c "COPY data_2022_oct FROM STDIN WITH (FORMAT csv, HEADER);"

# WITH (FORMAT csv, HEADER)
#                      ^ sets header to true, ignores the first line
#          ^ used to select csv parsing

# docker cp ../subject/customer/data_2022_oct.csv postgres:/home/file.csv
