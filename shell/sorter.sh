#!/bin/bash

for file in recovered/*
do
	if [[ $(file $file) == *"ASCII"* ]]
	then
		echo "/opt/$file,/opt/txt/$(basename $file),$(du -b $file | tr '\t' ' ' | cut -d' ' -f1)" >> report.csv
		mv $file txt
	elif [[ $(file $file) == *"image data"* ]]
	then
		echo "/opt/$file,/opt/img/$(basename $file),$(du -b $file | tr '\t' ' ' | cut -d' ' -f1)" >> report.csv
		mv $file img
	elif [[ $(file $file) == *"executable"* ]]
	then
		echo "/opt/$file,/opt/bin/$(basename $file),$(du -b $file | tr '\t' ' ' | cut -d' ' -f1)" >> report.csv
		mv $file bin	
	fi
done

