#from utilities import DRNAPTNcolors

def DRNAPTNcolors(seq):
    return str(seq).replace('A', '\033[1;31;43mA\033[m')\

t = DRNAPTNcolors('ATCG')

print('\033[1;31;43mAAAAAAA\033[m')
