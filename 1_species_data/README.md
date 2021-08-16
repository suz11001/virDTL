# Species Data

## Collecting Data

In this step we will collect the virus genomes as specified in [genomes.txt](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/input/genomes.txt)

The scripts are located [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/):
1. [1_fetchFasta.sh](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/1_fetchFasta.sh) --> fetches the genomes
2. [2_fetchCDS.sh](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/1_fetchCDS.sh) --> fetches the genome annotation (coding dna sequence) for each genome

The output is located [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/outputs/):
1. [1_genomes](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/outputs/1_genomes) --> all 54 genomes
2. [2_cds](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/outputs/2_cds) --> all possible cds annotated in ncbi for each genome

## Aligning Data

In this step we will align the whole genomes to generate a multiple sequence alignment (msa) and we will use [muscle](https://www.drive5.com/muscle/) to do this.  

First we have to concatnate all the genomes into a single file as shown [here](https://github.com/suz11001/virDTL/tree/main/https://github.com/suz11001/virDTL/blob/main/1_species_data/2_msa/1_cat.sh). The resulting file is [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/input/annotated_covids.fa)

Next we will use this [file](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/input/annotated_covids.fa) to generate a whole genome msa with this [script](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/2_muscle.sh).

The output of muscle is [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/2_msa/output/annotated_covids.aln)

## Build the Species Tree Using Whole Genome Alignment:

In this step we will create the species tree using the whole genome alignment generated in the previous step and [RAxML](https://cme.h-its.org/exelixis/web/software/raxml/). The script is [here](https://github.com/suz11001/virDTL/blob/main/1_species_data/3_raxml/1_raxml.sh).  

The resulting species tree is [this](https://github.com/suz11001/virDTL/blob/main/1_species_data/3_raxml/outputs/RAxML_bestTree.raxml) along with other RAxML output is [here](https://github.com/suz11001/virDTL/blob/main/1_species_data/3_raxml/outputs/)

## Root the Species Tree

We use [midpoint rooting](https://github.com/suz11001/virDTL/tree/main/1_species_data/4_root/midpoint.py) to root the [species tree](https://github.com/suz11001/virDTL/tree/main/1_species_data/4_root/annotated.tree). The rooted species tree is [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/4_root/annotated.tree_rooted)




