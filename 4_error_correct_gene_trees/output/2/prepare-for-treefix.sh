#!/bin/bash

input="../../inputs/genes.txt"
while IFS= read -r line
do
    echo $line
    mkdir $line
    cd $line/

    #copy all the files needed for gene tree error correction (treefix-dtl)
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

    # fix the alignment file to remove any IDs containing "." and "_" (must be done for tree-fix dtl)
    sed -i 's/\.//g' $line.aln
    sed -i 's/_//g' $line.aln

    # root the gene tree produced by raxml using opt root
    cat species.tree RAxML_bestTree.$line > optroot.input.txt

    ../../../software/ranger/CorePrograms/OptRoot.linux -i optroot.input.txt > optroot.output.txt 

    grep -A1 'All Optimal' optroot.output.txt > $line.tree
    sed -i 1d $line.tree
    
    #submit treefix-dtl script using the rooted gene tree
    sbatch treefix-dtl.sh $line.tree

done < "$input"
