#!/bin/bash

for j in {1..10}; do
	cat species.newick >> inputFile.newick
	cat gene$j.newick >> inputFile.newick
	mkdir OutputFiles$j
	for i in {1..10}; do
		./Ranger-DTL.linux --seed $i -i inputFile.newick -o OutputFiles$j/rangerOutput$i
	done
	./AggregateRanger.linux OutputFiles$j/rangerOutput >> AggregateOutput$j.txt
	rm inputFile.newick
done
