for ((i=1;i<=11;i++)); do
    line=$(head -n $i genes.txt | tail -n 1)
    j=1
    samples=(1 2 3 4 5 6 7 8 9 10)
    for sample in "${samples[@]}"; do
	../software/AggregateRanger_recipient.linux ./outputs/1_ranger/$sample/$line/"sample"$sample"_reconciliation" > ./outputs/2_aggregate/"AggregateRanger.sample_"$sample.$line.out.txt
    done 
done


