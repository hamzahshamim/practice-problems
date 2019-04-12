# write a function to generate all the possible k-mer combinations of DNA given k



#nucleotides = ['A', 'T', 'G', 'C']
#for i in range(1, 3):
#    combinations = itertools.product(*itertools.repeat(nucleotides, i))
#    for j in combinations:
#        print(j)



import itertools

def kmer(x):
    permut = itertools.permutations(["A", "T", "C", "G"],x)
    count_permut = []
    for i in permut:
            count_permut.append(i)
            print(count_permut.index(i)+1, i)
    print("number of permutations", len(count_permut))

kmer(5)

