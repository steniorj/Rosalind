
def gc_content(seq):
    '''GC content in a DNA/RNA sequence'''
    return ((seq.count('G') + seq.count('C'))/len(seq)*100)

print(gc_content('GCAAAAAAAA'))