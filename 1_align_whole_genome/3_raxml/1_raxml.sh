#!/bin/bash
#SBATCH --job-name=raxml
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 20
#SBATCH --mem=25G
#SBATCH -o raxml_%j.out
#SBATCH -e raxml_%j.err
#SBATCH --partition=general
#SBATCH --qos=general

module load anaconda
module load RAxML/8.2.11

raxmlHPC-PTHREADS -T 20 -f a -p 13579 -N 100 -m GTRGAMMA -x 12345 -s ../2_msa/output/annotated_covids.aln -n raxml
