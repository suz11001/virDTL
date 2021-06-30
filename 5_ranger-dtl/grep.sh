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
#SBATCH --mem=1G 

for ((i=1;i<=11;i++)); do
    line=$(head -n $i genes.txt | tail -n 1)
    echo "gene is $line"
    #grep -v "Transfers = 0" AggregateRanger.$line.out.txt | grep -w -E 'n3|NC0455122|n46|n48|n53'
    #for sample in {1..10}; do   
    samples=(1 2 3 4 5 6 7 8 9 10)
    for sample in "${samples[@]}"; do
	echo $sample
	grep "Transfers = 100" ./"AggregateRanger.sample_"$sample.$line.out.txt | grep -w -E 'n3|NC0455122|n49|n47|n46'   
    done
done


