for d in  ./test_* ; do
    file=`basename $d`
    echo $file
    python parse_agg.py $d > parsed_"$file".out
    #python parse_agg.py $d 
done
