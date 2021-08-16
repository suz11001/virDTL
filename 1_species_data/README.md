# Species Data

## Collecting Data

In this step we will collect the virus genomes as specified in [genomes.txt](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/input/genomes.txt)

The scripts are located [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/):
1. 1_fetchFasta.sh --> fetches the genomes
2. 2_fetchCDS.sh --> fetches the genome annotation (coding dna sequence) for each genome

The output is located [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/outputs/):
1. 1_genomes --> all 54 genomes
2. 2_cds --> all possible cds annotated in ncbi for each genome

## Aligning Data

In this step we will align the whole genomes to generate a multiple sequence alignment (msa) and we will use [muscle](https://www.drive5.com/muscle/) to do this.

First we have to concatnate all the genomes into a single file as shown [here]()