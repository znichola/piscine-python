#!/bin/bash

script_path="$(dirname $(realpath $0))"
cd $script_path

mkdir -p subject

if [ ! -e data_2023_feb.csv ]; then
    curl -O https://cdn.intra.42.fr/document/document/17077/data_2023_feb.csv 
fi

