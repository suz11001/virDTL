# VirDTL
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5247195.svg)](https://doi.org/10.5281/zenodo.5247195)


VirDTL is a computational protocol for inference of both ancestral and extant
strain recombination in viral genomes, using phylogenetic reconciliation.
Duplication-Transfer-Loss (DTL) reconciliation accounts for incongruencies
between the strain evolution tree and the evolutionary trees of each gene
family by inferring a history of gene duplications, gene losses, and
horizontal gene transfers (HGT). virDTL leverages DTL reconciliation to analyze incongruencies between the strain evolutionary tree and the evolutionary trees of each gene family (or genomic regions) to infer possible horizontal gene transfers, which correspond to possible recombination events in the context of viral evolution.


VirDTL is described in the paper ["virDTL: Viral recombination analysis through phylogenetic
reconciliation and its application to sarbecoviruses and
SARS-CoV-2"](https://compbio.engr.uconn.edu/wp-content/uploads/sites/2447/2022/07/virDTL_JCB2022_Preprint.pdf) by Zaman, Sledzieski, Berger, Wu, and Bansal.

If you use VirDTL in a publication, please cite

```
@article {ZamanVirDTL,
	author = {Zaman, Sumaira and Sledzieski, Samuel and Berger, Bonnie and Wu, Yi-Chieh and Bansal, Mukul S.},
	title = {virDTL: Viral recombination analysis through phylogenetic
reconciliation and its application to sarbecoviruses and
SARS-CoV-2},
	published = {Mary Ann Liebert},
	year = {2022},
	URL = {https://compbio.engr.uconn.edu/wp-content/uploads/sites/2447/2022/07/virDTL_JCB2022_Preprint.pdf},
	journal = {Journal of Computational Biology}
}
```

## Install
To install `virDTL` on Linux systems, run
```
source ./install.sh
```
This will create and activate the `virDTL` conda environment if it does not
exist, and will copy the required binaries from 
[`software`](https://github.com/suz11001/virDTL/tree/main/software)
to `~/.local/bin`.

To install the conda environment directly without installing the binaries, run
```
conda env create -f environment.yml
```

## Tutorial

- Download and pre-process sequence data as described [0_fetch_data](https://github.com/suz11001/virDTL/tree/main/0_fetch_data).  
- Generate a whole genome alignment as described in [1_align_whole_genome](https://github.com/suz11001/virDTL/tree/main/1_align_whole_genome)
- Annotate genes from each sequence, construct gene family alignments, and
estimate gene family trees with RAxML, using the scripts in [2_construct_gene_trees](https://github.com/suz11001/virDTL/tree/main/2_construct_gene_trees).  
- Generate multiple species trees using RAxML or BEAST (recommended) as described in [3_construct_species_tree](https://github.com/suz11001/virDTL/tree/main/3_construct_species_tree)
- Error correct gene family trees with [TreeFix-DTL](http://compbio.mit.edu/treefix/tutorial.html),
using the scripts in [4_error_correct_gene_trees](https://github.com/suz11001/virDTL/tree/main/4_error_correct_gene_trees).
- Reconcile the gene family trees with the strain tree with 
[RANGER-DTL](https://compbio.engr.uconn.edu/software/ranger-dtl/), using the 
scripts in 
[5_reconcile_gene_trees](https://github.com/suz11001/virDTL/tree/main/5_reconcile_gene_trees).
- Aggregate and summarize recombination events with support values, using the
scripts in 
[6_parse_reconciliation](https://github.com/suz11001/virDTL/tree/main/6_parse_reconciliation).
- Analyze the aggregate recombination events, using the notebooks in
[7_analysis](https://github.com/suz11001/virDTL/tree/main/7_analysis) or [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1W0zNutKE4sSduYw5hlYm7pgUCD-VSUBo?usp=sharing)

  - Compile aggregated recombinations and define support thresholds [here](https://github.com/suz11001/virDTL/blob/main/7_analysis/00_Clean_Aggregate_Recombinations.ipynb).
  - Compute basic statistics on transfers [here](https://github.com/suz11001/virDTL/blob/main/7_analysis/01_Basic_Statistics.ipynb).
  - Investigate bidirectional transfers [here](https://github.com/suz11001/virDTL/blob/main/7_analysis/02_Bidirectional_Transfers.ipynb).
  - Investigate recombination across gene boundaries [here](https://github.com/suz11001/virDTL/blob/main/7_analysis/03_Grouped_Transfers.ipynb).
  - Investigate relationship between clade size and rate of recombination [here](https://github.com/suz11001/virDTL/blob/main/7_analysis/04_Recombination_by_Clade_Size.ipynb).

Processed data sets from our analysis of the _Sarbecovirus_ subgenus can be
found in the corresponding folders.
