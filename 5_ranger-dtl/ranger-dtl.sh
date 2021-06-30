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

line=$(head -n "$SLURM_ARRAY_TASK_ID" genes.txt | tail -n 1)

samples=(1 2 3 4 5 6 7 8 9 10)

for sample in "${samples[@]}"; do
    mkdir -p ~/researchMukul/covid/13_beast_sp_tree_2/2_ranger/$sample
    cd ~/researchMukul/covid/13_beast_sp_tree_2/2_ranger/$sample
    mkdir $line
    cd $line/
    for ((i=1;i<=100;i++)); do
	~/researchMukul/pgtr/Linux/CorePrograms/Ranger-DTL.linux -q -i ~/researchMukul/covid/13_beast_sp_tree_2/1_treefix/$sample/$line/ranger.input.txt -o "sample"$sample"_reconciliation"$i
    done
done

