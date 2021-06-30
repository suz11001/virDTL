# (DendroPy) bash-4.2$ esearch -db nucleotide -query MT263074.1 | efetch -format fasta_cds_na > MT263074.1.fna
# (DendroPy) bash-4.2$ less MT263074.1.fna 
# (DendroPy) bash-4.2$ grep -c ">" MT263074.1.fna 
# 12
# (DendroPy) bash-4.2$ grep -c ">" MT263074.1.faa 
# 1
# (DendroPy) bash-4.2$ esearch -db nucleotide -query MT263074.1 | efetch -format fasta_cds_aa > MT263074.1.faa 
# source the dendropy environment
# esearch -db assembly -query NC_045512.2 | elink -target nuccore -name assembly_nuccore_insdc | elink -target protein | efetch -format fasta > test.faa

while read line <&3; do
    echo "$line"
    esearch -db nucleotide -query $line | efetch -format fasta_cds_na > cds/$line.fna
done 3<genomes.txt
