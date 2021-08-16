input="/home/FCAM/szaman/researchMukul/covid/genes.txt"
while IFS= read -r line
do
  echo "$line"
  mkdir -p test_"$line"_agg_regB
  cp ~/researchMukul/covid/13_beast_sp_tree_2/2_ranger/*/$line/sample*_reconciliation* test_"$line"_agg_regB
  cd test_"$line"_agg_regB
  for f in ./*; do mv "$f" "$f"_"$line"Prot; done
  cd ~/researchMukul/covid/utils/
done < "$input"
