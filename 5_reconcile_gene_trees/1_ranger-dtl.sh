
#change the path to virDTL in the $cwd variable
cwd="/virDTL/5_ranger-dtl/"


samples=(1 2 3 4 5 6 7 8 9 10)
for ((i=1;i<=11;i++)); do
    line=$(head -n $i genes.txt | tail -n 1)
    for sample in "${samples[@]}"; do
	mkdir -p $cwd/outputs/1_ranger/$sample
	cd $cwd/outputs/1_ranger/$sample
	mkdir $line
	cd $line/
	for ((i=1;i<=100;i++)); do
	    ../software/ranger/CorePrograms/Ranger-DTL.linux -q -i ../../../../../4_treefix/output/$sample/$line/ranger.input.txt -o "sample"$sample"_reconciliation"$i
    done
done

