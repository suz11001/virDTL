import sys
import os
import os.path
import subprocess
import dendropy
from dendropy import Tree
from dendropy.calculate import treecompare

def calcRF(t1,t2):
    cwd='/home/FCAM/szaman/researchMukul/pgtr/'
    tns = dendropy.TaxonNamespace()
    tree1=Tree.get_from_path(str(t1),"newick",taxon_namespace=tns,rooting='force-unrooted')
    tree2=Tree.get_from_path(str(t2),"newick",taxon_namespace=tns,rooting='force-unrooted')
    tree1.encode_bipartitions()
    tree2.encode_bipartitions()
    return (treecompare.unweighted_robinson_foulds_distance(tree1, tree2))
                    
if __name__ == "__main__":
    dist = calcRF(sys.argv[1],sys.argv[2])
    print(os.path.basename(sys.argv[1]))
    print(os.path.basename(sys.argv[2]))
    print(float(dist)/(2*(54-3)))
    print("###")
    
