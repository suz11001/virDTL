echo Installing virDTL conda environment...
CONDA_BASE=$(conda info --base)
source $CONDA_BASE/etc/profile.d/conda.sh

if $(conda env list | grep -q virDTL)
then
    conda deactivate
    conda activate virDTL
else
    conda deactivate
    conda env create -f environment.yml
    conda activate virDTL
fi

for i in $(find software/ranger | grep .linux)
do
    echo Copying $i to "$CONDA_PREFIX"/bin...
    cp $i "$CONDA_PREFIX"/bin
done

