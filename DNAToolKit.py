

# DNA toolkit file
from structures import *
from utilities import *


def validateSeq(dnaSeq,colors=True):
    tempSeq = dnaSeq.upper()
    for nuc in tempSeq:
        if nuc not in Nucleotides:
            return False
    if colors:
        return DRNAPTNcolors(tempSeq)
    else:
        return tempSeq


def CountNucFrequency(seq, colors=True):
    tempFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tempFreqDict[nuc] += 1
    if colors:
        return DRNAPTNcolors(tempFreqDict)
    else:
        return tempFreqDict


def transcribe(seq, colors=True):
    transcr = seq.replace("T", "U")
    if colors:
        return DRNAPTNcolors(transcr)
    else:
        return transcr


# Inverts sequence and make cDNA
def ComplDNA(seq,colors=True):
    if colors:
        return DRNAPTNcolors(''.join(DNA_ReverseComplement[nuc] for nuc in seq)[::-1])
    else:
        return ''.join(DNA_ReverseComplement[nuc] for nuc in seq)[::-1]


def gc_content(seq):
    '''GC content in a DNA/RNA sequence'''
    return ((seq.count('G') + seq.count('C'))/len(seq)*100)

def hammingDistance(seq1,seq2):
    '''Fuction that receive two strings for DNA/RNA segments and returns the number of mismatches. '''
    totalMismatch = 0
    for index ,value in enumerate(seq1):
        if seq2[index] != value:
            totalMismatch += 1
    return totalMismatch

def translate(seq,colors=True):
    '''Receives RNA string and return correspondant protein sequence'''
    ptn = ''
    codon = ''
    cont = 0
    for read in seq:
        if cont < 3:
            codon += read
            cont += 1
        if cont == 3:
            cont = 0
            for key, value in codon_dict.items():
                if codon == key:
                    ptn += value
                    codon = ''
    ptn = ptn.replace('Stop','')
    if colors:
        return DRNAPTNcolors(ptn)
    else:
        return ptn
