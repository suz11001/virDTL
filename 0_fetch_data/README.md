# Fetch Data

## Collecting Data From NCBI

In this step we will collect the virus genomes as specified in [genomes.txt](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/input/genomes.txt)

The scripts are located [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/):
1. [1_fetchFasta.sh](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/1_fetchFasta.sh) --> fetches the genomes
2. [2_fetchCDS.sh](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/1_fetchCDS.sh) --> fetches the genome annotation (coding dna sequence) for each genome

The output is located [here](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/outputs/):
1. [1_genomes](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/outputs/1_genomes) --> all 54 genomes
2. [2_cds](https://github.com/suz11001/virDTL/tree/main/1_species_data/1_genomes/outputs/2_cds) --> all possible cds annotated in ncbi for each genome
