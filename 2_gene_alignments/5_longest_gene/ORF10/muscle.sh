#!/bin/bash
#SBATCH --job-name=align
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 12
#SBATCH --mem=15G
#SBATCH -o align_%j.out
#SBATCH -e align_%j.err
#SBATCH --partition=general
#SBATCH --qos=general

module load muscle/3.8.31

f="M.fna"
out="M.aln"
muscle -in $f -maxiters 12 -out $out



