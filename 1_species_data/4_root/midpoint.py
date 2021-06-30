from ete3 import Tree
import numpy as np
import os
import sys


def midpointRooting(tree):
    rooted = tree.copy()
    rooted.set_outgroup(rooted.get_leaves()[0])
    rooted.set_outgroup(rooted.get_midpoint_outgroup())
    return rooted


tree = Tree(sys.argv[1])
rooted = midpointRooting(tree)
rooted.write(outfile=sys.argv[1]+'_rooted',format=1)
