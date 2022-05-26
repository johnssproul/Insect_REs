import os
from sys import argv

#       Take in accession number from the command line, from genomes.txt
file = argv[1]

#       Declare variables for each directory of buscos, add full path if needed
fragmented = file + '/fragmented_busco_sequences'
multi = file + '/multi_copy_busco_sequences'
single = file + '/single_copy_busco_sequences'
directories = [fragmented, multi, single]

#       Go into each directory and write each busco to outfile with header
writefile = file + "_busco_seqs"
with open(writefile, 'w') as outfile:
        for directory in directories:
                for filename in os.listdir(directory):
                        if filename.endswith('.fna'): 
                                fileinfo = filename[0:-4]
                                outfile.write('>' + fileinfo + '\n')
                                path = directory + '/' + filename
                                with open(path, 'r') as fna:
                                        line = fna.readline()
                                        for line in fna:
                                                if line.startswith('>'):
                                                        break
                                                line = line.strip()
                                                outfile.write(line)
                                        outfile.write('\n')
                                fna.close()
outfile.close()