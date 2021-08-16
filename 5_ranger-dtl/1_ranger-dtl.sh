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
#SBATCH --array=1-11%11

#change the path to virDTL in the $cwd variable
cwd="/virDTL/5_ranger-dtl/"

line=$(head -n "$SLURM_ARRAY_TASK_ID" genes.txt | tail -n 1)

samples=(1 2 3 4 5 6 7 8 9 10)

for sample in "${samples[@]}"; do
    mkdir -p $cwd/outputs/1_ranger/$sample
    cd $cwd/outputs/1_ranger/$sample
    mkdir $line
    cd $line/
    for ((i=1;i<=100;i++)); do
	../software/ranger/CorePrograms/Ranger-DTL.linux -q -i ../4_treefix/output/$sample/$line/ranger.input.txt -o "sample"$sample"_reconciliation"$i
    done
done

