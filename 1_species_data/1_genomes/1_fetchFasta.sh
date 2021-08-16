while read line <&3; do
    echo "$line"
    esearch -db nucleotide -query $line | efetch -format fasta > genomes/$line.fna
done 3<./input/genomes.txt
