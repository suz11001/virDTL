#!/bin/bash
#SBATCH --job-name=muscle
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 4
#SBATCH --mem=8G
#SBATCH -o muscle_%j.out
#SBATCH -e muscle_%j.err
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --array=1-6%6


module load muscle/3.8.31
line=$(head -n "$SLURM_ARRAY_TASK_ID" genes.txt  | tail -n 1)
mkdir -p $line
cd $line/
cp ../$line.fna ./$line.mod.fna
sed -i 's/\.//g' ./$line.mod.fna
sed -i 's/_//g' ./$line.mod.fna
echo $line.mod.fna
muscle -in $line.mod.fna -maxiters 12 -out $line.aln
