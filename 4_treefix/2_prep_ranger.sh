input="./inputs/genes.txt"

while IFS= read -r line
do
  echo "$line"
  samples=(1 2 3 4 5 6 7 8 9 10)
  for i in "${samples[@]}"
  do
      echo $i
      cd ./outputs/1_ranger/$i/$line
      cat $line.treefixDTL.tree | tr -d " \t\n\r" > $line.treefixDTL.mod.tree
      cat species.tree $line.treefixDTL.mod.tree > ranger.input.txt
      cd /virDTL/5_ranger-dtl/
  done
done < "$input"
