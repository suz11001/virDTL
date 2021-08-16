source activate  ~/.conda/envs/entrez
while read line <&3; do
    echo "$line"
    esearch -db nucleotide -query $line | efetch -format fasta_cds_na > outputs/2_cds/$line.fna
done 3<./input/genomes.txt
