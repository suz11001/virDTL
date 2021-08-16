# Constructing Species Trees

## Estimate Species Trees
To construct species trees for the non-recombinant regions, use BEAST with the provided config files
```
beast species_tree_configs/beast_NRR_B_config.xml
```

## Date Species Trees
To date the species tree, again use BEAST
```
beast species_tree_configs/beast_NRR_B_dating_config.xml
```

BEAST may need to be run multiple times or for longer iterations to ensure
that the chain converges -- multiple runs can be combined using `TreeAnnotator`
(not included with `virDTL`).

