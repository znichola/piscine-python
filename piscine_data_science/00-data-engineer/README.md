# the data engineer

Creation of a DB

## Quick start

- `make up` to launch the containers
- navigate to [`localhost:80`](localhost:80) for th3 pgadmin portal
- login through tphe browser
- then create a new database, use the database credentials from the .env
- use the ip adress of the container, find it with `make ip`
- `./download_data.sh` to get the data for the project

## Docker commands

Copy local file to the container
```bash
docker cp ../subject/customer/data_2022_oct.csv postgres:/home/file.csv
```

## PostgreSQL commands

List the tables in the db
```psql
\dt
```

Show only 10 rows from the table
```psql
SELECT * FROM data_2022_dec LIMIT 10;
```

Delete the contents of a table
```paql
TRUNCATE data_2022_dec;
```

Delete a table
```psql
DROP TABLE data_2022_dec CASCADE;
```

Delete many tables
```psql
DROP TABLE IF EXISTS data_2022_dec, data_2022_nov, data_2022_oct, data_2023_jan CASCADE;
```

Select rows that are not null
```psql
SELECT * FROM item WHERE category_code IS NOT NULL LIMIT 10
```

Copy a csv file to a table
```psql
COPY data_2022_dec FROM '/subject/customer/data_2022_dec.csv' (FORMAT csv, HEADER);
```
COPY vs /copy Do not confuse COPY with the psql instruction \copy. \copy invokes COPY FROM STDIN or COPY TO STDOUT, and then fetches/stores the data in a file accessible to the psql client. Thus, file accessibility and access rights depend on the client rather than the server when \copy is used.
`WITH (FORMAT csv, HEADER)`: `FORMAT` used to select csv parsing `HEADER` sets header to true, ignores the first line

Count the number of rown in the table
```psql
SELECT COUNT(*) FROM data_2022_dec;
```

Create temprary database for testing
```psql
CREATE TEMP TABLE temp_data AS
SELECT * FROM customers;
```