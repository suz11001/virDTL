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
line=$(head -n "$SLURM_ARRAY_TASK_ID"  ~/researchMukul/covid/12_beast_sp_tree/genes.txt | tail -n 1)
echo $line
mkdir $line
cd $line/

cp ~/researchMukul/covid/5_gene_alignments/5_longest_gene/$line/RAxML_bestTree.$line.tree ./RAxML_bestTree.$line
cp ~/researchMukul/covid/5_gene_alignments/5_longest_gene/$line/$line.aln ./
cp ~/researchMukul/covid/13_beast_sp_tree_2/species.tree species.tree
cp ~/researchMukul/covid/8_treefix-DTL/mapping.txt ./
cp ~/researchMukul/covid/8_treefix-DTL/treefix-dtl.sh ./

#remove branch lengths that are as :*,
sed -i -e 's/:[^:,]*,/,/g' RAxML_bestTree.$line
#remove branch lengths that are as :*)
sed -i -e 's/:[^:)]*)/)/g' RAxML_bestTree.$line
sed -i -e 's/:[^:;]*;/;/g' RAxML_bestTree.$line
sed -i -e 's/\.*//g' RAxML_bestTree.$line
sed -i -e 's/NC_/NC/g' RAxML_bestTree.$line

#use the above tree as an input to opt root

# fix aln
sed -i 's/\.//g' $line.aln
sed -i 's/_//g' $line.aln

cat species.tree RAxML_bestTree.$line > optroot.input.txt

~/researchMukul/pgtr/Linux/CorePrograms/OptRoot.linux -i optroot.input.txt > optroot.output.txt 

grep -A1 'All Optimal' optroot.output.txt > $line.tree
sed -i 1d $line.tree

sbatch treefix-dtl.sh $line.tree

