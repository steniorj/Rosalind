from DNAToolKit import *

DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

def ComplDNA(seq,colors=True):
    if colors:
        return DRNAPTNcolors(''.join(DNA_ReverseComplement[nuc] for nuc in seq)[::-1])
    else:
        return ''.join(DNA_ReverseComplement[nuc] for nuc in seq)[::-1]

print(ComplDNA('ATCGATCG'))