for f1 in *.sars_rooted
do
    sum=0
    echo "Processing $f1 file.." 
    for f2 in *.sars_rooted
    do
	echo "comparing again $f2"
	python ../calcRF.py $f1 $f2
    done
done
