#!/bin/bash
#SBATCH --job-name=raxml
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --mem=1G
#SBATCH -o bash_%j.out
#SBATCH -e bash_%j.err
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --array=1-10%3


echo $SLURM_ARRAY_TASK_ID
mkdir ./output/$SLURM_ARRAY_TASK_ID
cd ./output/$SLURM_ARRAY_TASK_ID
cp ../../inputs/edit.sh ./
sbatch edit.sh

