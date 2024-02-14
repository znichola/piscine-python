#!/bin/bash

filename=subject.zip
# filename=population_total.csv

if [ ! -e $filename ]; then
    curl -L -O https://cdn.intra.42.fr/document/document/23498/subject.zip
fi

unzip $filename
