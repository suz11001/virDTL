## Error Correcting Gene Trees

In this step we will be error correcting the gene trees using the following as input:  
1. Gene tree (an unrooted gene tree was generated in step [2](https://github.com/suz11001/virDTL/tree/main/2_construct_gene_trees)  
2. The sequence alignment of the gene family  
3. Species tree  
4. A gene to species mapping file - each gene name must correspond to a species  

The error-correcting will be done by TreeFix-DTL, for each gene family. Due to multiple optimal topologies existing, we will run Treefix-DTL 10 times to generate the gene tree topology sample space.  

The scripts serve the following purpose:
[1_master.sh](https://github.com/suz11001/virDTL/blob/main/4_error_correct_gene_trees/1_master.sh) - generates a directory for each sample (1,2,...,10) and copies the script [prepare-for-treefix.sh](https://github.com/suz11001/virDTL/tree/main/4_error_correct_gene_trees/inputs/prepare-for-treefix.sh) in each sample directory. [prepare-for-treefix.sh](https://github.com/suz11001/virDTL/tree/main/4_error_correct_gene_trees/inputs/prepare-for-treefix.sh) then creates a directory for each gene family and copies of the relevant files (gene trees, sequence alignment, species tree, and mapping file). It also modifies these files so that they are accepted by TreeFix-DTL. Finally, the script submits [treefix-dtl.sh](https://github.com/suz11001/virDTL/blob/main/4_error_correct_gene_trees/inputs/treefix-dtl.sh) which executes treefix-dtl.

[2_prep_ranger.sh](https://github.com/suz11001/virDTL/blob/main/4_error_correct_gene_trees/2_prep_ranger.sh) - this script takes the output from TreeFix (error-correct gene tree), cleans it up and roots the TreeFix gene tree and concatenates it with the species tree. The file it produces (ranger.input.txt) is the file used as input for ranger.

