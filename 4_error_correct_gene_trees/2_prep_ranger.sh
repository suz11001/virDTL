input="./inputs/genes.txt"

#change the $cwd to variable to the FULL path of where virDTL is located
cwd="/home/"

while IFS= read -r line
do
  echo "$line"
  samples=(1 2 3 4 5 6 7 8 9 10)
  for i in "${samples[@]}"
  do
      echo $i
      cd ./outputs/1_ranger/$i/$line
      #remove new line characters from tree fix tree
      cat $line.treefixDTL.tree | tr -d " \t\n\r" > $line.treefixDTL.mod.tree

      #root the tree-fix tree
      ../../../software/ranger/CorePrograms/OptRoot.linux -i $line.treefixDTL.mod.tree > treefix.optroot.out
      grep -A1 'All Optimal'  > treefix.optroot.out

      #put the species tree and rooted tree fix tree in a single file (ranger.input.txt)
      cat species.tree > ranger.input.txt
      sed 1d treefix.optroot.out >> ranger.input.txt

      cd $cwd/virDTL/5_ranger-dtl/
  done
done < "$input"
