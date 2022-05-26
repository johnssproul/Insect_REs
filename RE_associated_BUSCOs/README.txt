#scripts for this analysis were copied to this repository from https://github.com/AshlynPowell/busco_repeats and written by Ashlyn Powell

#condense_buscos.py compiles BUSCO sequences from a given assembly into a single file. The script takes in an accession number, opens each sequence file in the associated BUSCO results, and writes each sequence to an outfile formatted for BLAST (if a multi-copy BUSCO, only the first sequence is written to the file).

#busco_blast_bokeh.sh runs blast calls and bokeh visualization scripts. Comments in the scripts describe command line arguements that should be passed in to each script.

#visualize_busco_blast.sh does calculations to determine which BUSCOs fit criteria for being an "RE-associated BUSCO", also uses bokeh to visualize data in multiple ways (histogram, lineplot, table) which we used to sanity check that our methods (e.g., calculating baseline from first 3 quartiles of data) were appropriate given distribution of values across all samples.

#genomes.txt contains a list of all 441 insect genome assemblies used in this study. You can run the other scripts over this list, e.g. for i in cat genomes.txt; do python visualize_busco_blast.py $i; done  