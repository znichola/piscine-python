#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage $0 bit.ly/link"
  exit 1
fi

# curl
# -s or --silent  no printing of progress
# -I or --head    is for only the header

# cut
# -c  to cut at characters
# 11- to cut at  the 11th character and select those that follow

result=$(curl -Is "$1" | grep "Location" | cut -c 11-)

echo $result
