#!/bin/bash
# Submission script for Xanadu 
#SBATCH --job-name=treefix
#SBATCH -o treefix-%j.output
#SBATCH -e treefix-%j.error
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH --ntasks=1 
#SBATCH --cpus-per-task=8
#SBATCH --partition=general
#SBATCH --qos=general 
#SBATCH --mem=40G 

source ~/.bashrc

treefixDTL \
    -s species.tree \
    -S mapping.txt \
    -A .aln \
    -o .tree \
    -n .treefixDTL.tree \
    -U .tree \
    -e "-m GTRGAMMA -e 2.0" \
    -V1 -l ./$line.nuc.raxml.treefixDTL.log \
    $1
