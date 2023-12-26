#!/bin/bash

read -p "Enter desired db password : " pgpassword

if [ -z "$pgpassword" ]; then
    echo "pgPassword can't be empty, bye"
    exit 42
fi

read -p "Enter desired admire password : " adpassword

if [ -z "$adpassword" ]; then
    echo "adpassword can't be empty, bye"
    exit 42
fi

printf "#auto generated with gen_env.sh
POSTGRES_DB=piscineds
POSTGRES_USER=$USER
POSTGRES_PASSWORD=$pgpassword
PGADMIN_DEFAULT_EMAIL=$USER@42
PGADMIN_DEFAULT_PASSWORD=$adpassword
" > .env
