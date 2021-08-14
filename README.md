# VirDTL

VirDTL is a computational protocol for inference of both ancestral and extant
strain recombination in viral genomes, using phylogenetic reconciliation.
Duplication-Transfer-Loss (DTL) reconciliation accounts for incongruencies
between the strain evolution tree and the evolutionary trees of each gene
family by inferring a history of gene duplications, gene losses, and
horizontal gene transfers (HGT). In the viral setting, HGTs correspond to
viral recombinations, so DTL reconciliation can be used to infer
recombination. 

VirDTL is described in the paper ["Phylogenetic reconciliation reveals 
extensive ancestral recombination in sarbecoviruses and the SARS-CoV-2 
lineage"](https://www.biorxiv.org/content/10.1101/2021.08.12.456131v1) by Zaman, Sledzieski, Berger, Wu, and Bansal.

If you use VirDTL in a publication, please cite

```
@article {ZamanVirDTL,
	author = {Zaman, Sumaira and Sledzieski, Samuel and Berger, Bonnie and Wu, Yi-Chieh and Bansal, Mukul S.},
	title = {Phylogenetic reconciliation reveals extensive ancestral recombination 
  in Sarbecoviruses and the SARS-CoV-2 lineage},
	year = {2021},
	doi = {10.1101/2021.08.12.456131},
	publisher = {Cold Spring Harbor Laboratory},
	URL = {https://www.biorxiv.org/content/early/2021/08/12/2021.08.12.456131},
	journal = {bioRxiv}
}
```

## Tutorial

- Download and pre-process sequence data, and construct the full strain tree
with [RAxML](https://cme.h-its.org/exelixis/web/software/raxml/)
or [BEAST](https://beast.community) (recommended), using the scripts in
[1_species_data](https://github.com/suz11001/virDTL/tree/main/1_species_data).
- Annotate genes from each sequence, construct gene family alignments, and
estimate gene family trees with RAxML, using the scripts in
[2_gene_alignements](https://github.com/suz11001/virDTL/tree/main/2_gene_alignments).
- Error correct gene family trees with [TreeFix-DTL](http://compbio.mit.edu/treefix/tutorial.html),
using the scripts in 
[4_treefix](https://github.com/suz11001/virDTL/tree/main/4_treefix).
- Reconcile the gene family trees with the strain tree with 
[RANGER-DTL](https://compbio.engr.uconn.edu/software/ranger-dtl/), using the 
scripts in 
[5_ranger-dtl](https://github.com/suz11001/virDTL/tree/main/5_ranger-dtl).
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
