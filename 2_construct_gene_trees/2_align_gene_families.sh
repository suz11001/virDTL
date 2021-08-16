input="genes.txt"
while IFS= read -r line
do
    mkdir -p outputs/1_alignments/$line
    cd outputs/1_alignments/$line
    cp ../../../inputs/$line/$line.fna ./$line.mod.fna
    # edit the alignment to remove "." and "_" characters - muscle does not accept them
    sed -i 's/\.//g' ./$line.mod.fna
    sed -i 's/_//g' ./$line.mod.fna
    # run muscle
    muscle -in $line.mod.fna -maxiters 12 -out $line.aln
    cd ../../../
done < "$input"
