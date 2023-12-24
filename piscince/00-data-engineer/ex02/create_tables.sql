CREATE TABLE data_2022_oct (
    event_time TIMESTAMP NOT NULL,
    event_type VARCHAR(255) NOT NULL,
    product_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    user_id INTEGER NOT NULL,
    user_session VARCHAR(255) NOT NULL
);

\copy data_2022_oct FROM /home/data_2022_oct.csv  WITH (FORMAT csv, HEADER);