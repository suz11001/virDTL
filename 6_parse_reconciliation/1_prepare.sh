input="../4_treefix/inputs/genes.txt"
while IFS= read -r line
do
  echo "$line"
  mkdir -p outputs/test_"$line"_agg_regB
  #copy reconcilation files into a single location
  cp ../5_ranger-dtl/outputs/1_ranger/*/$line/sample*_reconciliation* test_"$line"_agg_regB
  #go to the location
  cd test_"$line"_agg_regB
  #add the protein name on to the files that were just copied
  for f in ./*; do mv "$f" "$f"_"$line"Prot; done
  cd ../
done < "$input"
