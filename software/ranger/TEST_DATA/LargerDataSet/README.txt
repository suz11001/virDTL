Here we provide a larger simulated dataset with a species tree (species.newick) of 100 taxa and 10 rooted gene trees (gene1.newick, gene2.newick, ...) evolved inside this species tree under a probabilistic model of gene duplication, transfer, and loss. The sample Bash script (bash.sh) included with this dataset shows how to automate the analysis of all gene tree in this dataset. Specifically, the Bash cript iterates through the 10 gene tree files, computes 100 optimal reconciliations (sampled uniformly at random) for each gene tree using Ranger-DTL, and uses AggregateRanger to aggregate these 100 optimal reconciliations and produce an AggregateOutput.txt file for each gene tree. This script can be easily customized to handle smaller or larger datasets, unrooted gene trees, fewer or larger number of sampled optimal reconciliations, etc. 

For example, if there is only one gene tree (gene.newick) to analyze and this gene tree is unrooted, then the following Bash script code can be used to root this gene tree optimally (randomly chosen optimal if there are multiple optimal roots), compute 50 optimal reconciliations, and then aggregate the samples into a single reconciliation file (AggregateOutput.txt). 

#!/bin/bash
cat species.newick >> tempFile.newick
cat gene.newick >> tempFile.newick
cat species.newick >> inputFile.newick
./OptRoot.linux -r -i tempFile.newick | grep ";" >> inputFile.newick
rm tempFile.newick
mkdir OutputFiles
for i in {1..50}; do
	./Ranger-DTL.linux --seed $i -i inputFile.newick -o OutputFiles/rangerOutput
done
./AggregateRanger.linux OutputFiles/rangerOutput >> AggregateOutput.txt
rm inputFile.newick


If the user would like to aggregate accross all possible optimal gene tree rootings, then the summary Python script SummarizeOptRootings.py should be used instead.   
