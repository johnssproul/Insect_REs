#!/bin/bash

#SBATCH --time=72:00:00   # walltime
#SBATCH --ntasks=1   # number of processor cores (i.e. tasks)
#SBATCH --nodes=1   # number of nodes
#SBATCH --mem-per-cpu=4096M   # memory per CPU core
#SBATCH -J "busco_data.job"   # job name
#SBATCH --mail-user=ashlynpowell913@gmail.com   # email address
#SBATCH --mail-type=FAIL


# Set the max number of threads to use for programs using OpenMP. Should be <= ppn. Does nothing if the program doesn't use OpenMP.
export OMP_NUM_THREADS=$SLURM_CPUS_ON_NODE

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE


source ~/.bashrc
conda activate blast

#	If files are in different directories add full path to each
#	Script takes in name of the genome (query should be genome + _busco_seqs) from the command line
#	And names the output file: genome + .blast.out

#	Make blast database if needed with the following command:
#		makeblastdb -dbtype nucl -in $1

blastn -db $1 -query $1_busco_seqs -out $1.blast.out -outfmt 7

#	Visualize blast results with bokeh script
conda activate bokeh
python visualize_busco_blast.py $1.blast.out
