echo "# Installing virDTL conda environment"
if $(conda env list | grep -q virDTL)
then
    conda deactivate
    conda activate virDTL
else
    conda deactivate
    conda env create -f environment.yml
    conda activate virDTL
fi

echo "# Installing Ranger-DTL"
for i in $(find software/ranger | grep .linux)
do
    echo Copying $i to "$CONDA_PREFIX"/bin
    cp $i "$CONDA_PREFIX"/bin
done

echo "# Installing TreeFix-DTL"
export PYTHONPATH=$PYTHONPATH:$(pwd)/software/TreeFix/sw/lib64/python2.7/site-packages
for i in $(find software/TreeFix/sw/bin/*)
do
    echo Copying $i to "$CONDA_PREFIX"/bin
    cp $i "$CONDA_PREFIX"/bin
done