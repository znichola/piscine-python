#!/bin/bash

read -p "Enter desired db password : " password

if [ -z "$password" ]; then
    echo "Password can't be empty, bye"
    exit 42
fi

printf "#auto generated with gen_env.sh
POSTGRES_DB=piscineds
POSTGRES_USER=znichola
POSTGRES_PASSWORD=$password
" > .env