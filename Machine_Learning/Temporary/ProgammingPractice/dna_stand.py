def DNA_strand(dna):
    dict={'A':'T','T':'A','C':'G','G':'C'}
    return "".join([dict[e] for e in dna  ])


print (DNA_strand('ATTGC'))

