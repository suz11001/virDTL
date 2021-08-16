# Constructing Species Trees

## Estimate Species Trees
To construct species trees for the non-recombinant regions, use BEAST with the provided config files
```
beast species_tree_configs/beast_NRR_B_config.xml
```

You can create your own files using `beauti`. To create an accurate species
tree, ensure you are using a non-recombinant region, include known tip dates,
and set a reasonable prior for rates of evolution (see manuscript _Methods_
for details on how these were set for the _Sarbecovirus_) analysis.

## Date Species Trees
To date the species tree, again use BEAST
```
beast species_tree_configs/beast_NRR_B_dating_config.xml
```

BEAST may need to be run multiple times or for longer iterations to ensure
that the chain converges -- multiple runs can be combined using `TreeAnnotator`
(not included with `virDTL`).

## Root Trees using Midpoint Rooting

BEAST returns rooted trees, and for the _Sarbecovirus_ analysis, we rooted
them using a known outgroup. However, in general you can also perform
alternative rootings of the species tree, including midpoint rooting:

```
python midpoint.py <species tree file>
```

write out `<species tree file>.rooted` as the midpoint rooted tree.
