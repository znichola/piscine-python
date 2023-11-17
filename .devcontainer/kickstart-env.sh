#!/bin/bash

echo "re-generate .env, old one gets overwritten (yes/no)"

read confirmation

if [ "$confirmation" == "yes" ] || [ "$confirmation" == "y" ]; then
    echo "Generating ..."
else
    echo "ok, bye"
    exit 0
fi

{
    printf "\
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=postgres
POSTGRES_HOST=localhost
"
} > .env
