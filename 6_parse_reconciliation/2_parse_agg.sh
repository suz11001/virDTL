for d in  ./inputs/test_* ; do
    file=`basename $d`
    echo $file
    python parse_agg.py $d > ./outputs/parsed_"$file".out
done
