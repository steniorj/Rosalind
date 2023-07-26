# DNA Toolest/Code testing file
from DNAToolKit import *
import random

# Creating a random DNA string for testing
rndDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(5)])

DNAStr = (validateSeq(rndDNAStr))
print(CountNucFrequency(DNAStr))