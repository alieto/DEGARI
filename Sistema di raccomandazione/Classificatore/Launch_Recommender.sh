#!/bin/bash

#Bash script to run DENOTER's Recommender
#on all combined concepts prototypes

#syntax: ./Launch_Recommender [folder]*
#							  *optional


#load prototype files' names from parameter folder
#(default folder is ../prototipi)

folder=${1:-../prototipi}
prototypes=( `ls ${folder}` )

#clears resume files
rm recommendations.tsv
rm resume.tsv

#runs Recommender on each prototype
for (( i = 0 ; i < ${#prototypes[@]} ; i += 1 )) ; do
    python3 Recommender.py ${folder}/${prototypes[$i]}
done

python3 count.py
