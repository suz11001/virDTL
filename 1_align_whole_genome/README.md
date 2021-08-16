## Aligning Data

In this step we will align the whole genomes to generate a multiple sequence alignment (msa) and we will use [muscle](https://www.drive5.com/muscle/) to do this.  

First we have to concatnate all the genomes into a single file as shown [here](https://github.com/suz11001/virDTL/tree/main/https://github.com/suz11001/virDTL/blob/main/1_species_data/2_msa/1_cat.sh). The resulting file is [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/input/annotated_covids.fa)

Next we will use this [file](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/input/annotated_covids.fa) to generate a whole genome msa with this [script](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/2_muscle.sh).

The output of muscle is [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/output/annotated_covids.aln)





