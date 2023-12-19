#!/bin/bash

filename=subject.zip
# filename=population_total.csv

if [ ! -e $filename ]; then
    curl -O https://cdn.intra.42.fr/document/document/17117/subject.zip
# curl -O https://cdn.intra.42.fr/document/document/15948/population_total.csv
fi

unzip $filename
