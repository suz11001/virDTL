#activate the conda environment in which entrez is installed
source activate  ~/.conda/envs/entrez

while read line <&3; do
    echo "$line"
    esearch -db nucleotide -query $line | efetch -format fasta > outputs/1_genomes/$line.fna
done 3<./input/genomes.txt
