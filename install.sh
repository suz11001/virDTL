#!/usr/bin/bash
for i in $(find software/ranger | grep .linux)
do
    echo Copying $i to "$CONDA_PREFIX"/bin
    cp $i "$CONDA_PREFIX"/bin
done
