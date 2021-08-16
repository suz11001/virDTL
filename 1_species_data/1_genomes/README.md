These genomes were selected for their completeness and their (mostly completely)  annotations i.e. if cds could not be successfully retrieved from esearch (as directed by script X), we had to drop the genomes.  

Using these script requires the esearch program which can be installed through conda:  
#create a virtual conda environment called entrez
conda create -n entrez
#install the entrez module in the virtual environment created in the previous step  
conda install -n entrez -c bioconda entrez-direct
#activate this environment in the shell script fetching the genomes and cds annotation  

