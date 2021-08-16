#!/bin/bash
# Submission script for Xanadu 
#SBATCH --job-name=ranger
#SBATCH -o ranger-%j.output
#SBATCH -e ranger-%j.error
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=1
#SBATCH --partition=general
#SBATCH --qos=general 
#SBATCH --mem=5G 

for ((i=1;i<=11;i++)); do
    line=$(head -n $i genes.txt | tail -n 1)
    mkdir -p agg_$line
    j=1
    samples=(1 2 3 4 5 6 7 8 9 10)
    for sample in "${samples[@]}"; do
	~/researchMukul/pgtr/AggregateRanger_recipient.linux ./outputs/$sample/$line/"sample"$sample"_reconciliation" > "AggregateRanger.sample_"$sample.$line.out.txt
    done 
done


