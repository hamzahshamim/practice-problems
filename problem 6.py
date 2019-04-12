# given two genomic regions, write a function to determine if they overlap (dont worry about strand)
import itertools
from itertools import count, groupby
def overlap(reg1, reg2):
    d = 0
    t = list()
    while d < len(reg1):
        if reg1[d] == reg2[d]:
            t.append(d+1)
        d = d+1
    G = (list(x) for _, x in groupby(t, lambda x, c=count(): next(c) - x))
    print ",".join("-".join(map(str, (g[0], g[-1])[:len(g)])) for g in G)


overlap("ATGATCCATGCATGCAAAAAAATGCATGCACCCTGC","ATGCTACATGCATGCAAAAAAATGCATGCATTTTGC")



