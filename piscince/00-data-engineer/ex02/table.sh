#!/bin/bash

# script_path="$(dirname $(realpath $0))"
# source $script_path/../.env

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
        -c "COPY data_2022_oct FROM /subject/customer/data_2022_dec.csv (FORMAT csv, HEADER);"

# COPY vs /copy
    # Do not confuse COPY with the psql instruction \copy. \copy 
    # invokes COPY FROM STDIN or COPY TO STDOUT, and then 
    # fetches/stores the data in a file accessible to the psql client. 
    # Thus, file accessibility and access rights depend on the 
    # client rather than the server when \copy is used.

# WITH (FORMAT csv, HEADER)
#                      ^ sets header to true, ignores the first line
#          ^ used to select csv parsing

# docker cp ../subject/customer/data_2022_oct.csv postgres:/home/file.csv
