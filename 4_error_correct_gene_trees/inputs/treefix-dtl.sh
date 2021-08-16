#!/bin/bash

treefixDTL \
    -s species.tree \
    -S mapping.txt \
    -A .aln \
    -o .tree \
    -n .treefixDTL.tree \
    -U .tree \
    -e "-m GTRGAMMA -e 2.0" \
    -V1 -l ./$line.nuc.raxml.treefixDTL.log \
    $1
