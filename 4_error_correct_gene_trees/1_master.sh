samples=(1 2 3 4 5 6 7 8 9 10)
for sample in "${samples[@]}"; do
    echo $sample
    mkdir ./output/$sample
    cd ./output/$sample
    cp ../../inputs/prepare-for-treefix.sh ./
    sbatch prepare-for-treefix.sh
    cd ../../
done

