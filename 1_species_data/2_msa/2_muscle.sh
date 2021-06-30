#!/bin/bash
#SBATCH --job-name=msa
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 12
#SBATCH --mem=20G
#SBATCH -o msa_%j.out
#SBATCH -e msa_%j.err
#SBATCH --partition=general
#SBATCH --qos=general

module load muscle/3.8.31

muscle -in annotated_covids.fa -maxiters 12 -out annotated_covids.aln



