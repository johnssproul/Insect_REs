#!/bin/bash

#loops through .tbl files in directory and runs parser script. .tbl files are 
#available in FigShare doi associated with this study.

for i in *tbl 
do 
	python3 RM_table_parser_families_mod4.py $i repeatmasker_results_fam.txt 
done