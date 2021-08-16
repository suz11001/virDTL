#!/bin/bash
#SBATCH --job-name=treefix
#SBATCH --mail-user=sumaira.zaman@uconn.edu
#SBATCH --mail-type=ALL
#SBATCH -n 1
#SBATCH -N 1
#SBATCH -c 1
#SBATCH --mem=5G
#SBATCH -o edit_%j.out
#SBATCH -e edit_%j.err
#SBATCH --partition=general
#SBATCH --qos=general
#SBATCH --array=1-11%5

echo $SLURM_ARRAY_TASK_ID
line=$(head -n "$SLURM_ARRAY_TASK_ID"  ../../inputs/genes.txt | tail -n 1)
echo $line
mkdir $line
cd $line/

cp ../../../../2_gene_alignments/outputs/2_trees/$line/RAxML_bestTree.$line.tree ./RAxML_bestTree.$line
cp ../../../../2_gene_alignments/outputs/2_trees/$line/$line.aln ./
cp ../../../inputs/NRRB.tree species.tree
cp ../../../inputs/mapping.txt ./
cp ../../../inputs/treefix-dtl.sh ./

#remove branch lengths that are as :*,
sed -i -e 's/:[^:,]*,/,/g' RAxML_bestTree.$line
#remove branch lengths that are as :*)
sed -i -e 's/:[^:)]*)/)/g' RAxML_bestTree.$line
sed -i -e 's/:[^:;]*;/;/g' RAxML_bestTree.$line
sed -i -e 's/\.*//g' RAxML_bestTree.$line
sed -i -e 's/NC_/NC/g' RAxML_bestTree.$line

#use the above tree as an input to opt root

# fix the alignment file to remove any IDs containing "." and "_" 
sed -i 's/\.//g' $line.aln
sed -i 's/_//g' $line.aln

cat species.tree RAxML_bestTree.$line > optroot.input.txt

../../../software/ranger/CorePrograms/OptRoot.linux -i optroot.input.txt > optroot.output.txt 

grep -A1 'All Optimal' optroot.output.txt > $line.tree
sed -i 1d $line.tree

sbatch treefix-dtl.sh $line.tree

