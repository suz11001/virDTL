input="genes.txt"
while IFS= read -r line
do	
    mkdir -p outputs/2_trees/$line
    cd outputs/2_trees/$line	
    raxmlHPC-PTHREADS -T 8 -f a -p 13579 -N 100 -m GTRGAMMA -x 12345 -s ../../1_alignments/$line/$line.aln -n $line.tree
    cd ../../../
done < "$input"
