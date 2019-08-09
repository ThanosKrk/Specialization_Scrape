#!/bin/bash

input="./specializations.txt"
COUNTER=0

# Installing BeautifulSoup4 module
pip3 -q install BeautifulSoup4

# Create folder for results
if [ -e "./specializations" ]; then
	echo "Specializations directory exists"
else
	echo "Creating specializations folder"
	mkdir specializations
fi

# Executing python script to create files
while IFS= read -r line; do
	COUNTER=$((COUNTER+1))
	python3 discrape.py "$line" $COUNTER &
done < "$input"

