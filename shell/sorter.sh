#!/bin/bash

# final exam: 2000 files needs to be sorted to their respective directories based on their file type
# report.csv contains information about original directory, new directory and file size


echo "ORIGINAL_DIR,NEW_DIR,SIZE_BYTES" > report.csv

for file in recovered/*
do
	if [[ $(file "$file") == *"ASCII"* ]]  # varianta: if [[ $(file "$file" | grep ASCII) ]]
	then
		DIR=txt
	elif [[ $(file "$file") == *"image data"* ]]  # varianta: if [[ $(file "$file" | grep "image data") ]]
	then
		DIR=img
	elif [[ $(file "$file") == *"executable"* ]]  # varianta: if [[ $(file "$file" | grep "executable") ]]
	then
		DIR=bin	
	fi
	echo "/opt/$file,/opt/$DIR/$(basename $file),$(du -b $file | tr '\t' ' ' | cut -d' ' -f1)" >> report.csv
	mv "$file" $DIR
done

