#DNA/RNA with colors
def DRNAPTNcolors(seq):
    return str(seq).replace('A', '\033[92mA\033[m')\
        .replace('U', '\033[91mU\033[m')\
        .replace('C', '\033[94mC\033[m')\
        .replace('G', '\033[93mG\033[m')\
        .replace('T', '\033[91mT\033[m')\
        .replace('B', '\033[92mB\033[m')\
        .replace('D', '\033[91mD\033[m')\
        .replace('F', '\033[94mF\033[m')\
        .replace('H', '\033[93mH\033[m')\
        .replace('I', '\033[91mI\033[m')\
        .replace('J', '\033[91mJ\033[m')\
        .replace('K', '\033[94mK\033[m')\
        .replace('L', '\033[93mL\033[m')\
        .replace('M', '\033[91mM\033[m')\
        .replace('N', '\033[92mN\033[m')\
        .replace('O', '\033[91mO\033[m')\
        .replace('P', '\033[94mP\033[m')\
        .replace('Q', '\033[93mQ\033[m')\
        .replace('R', '\033[94mR\033[m')\
        .replace('S', '\033[33mS\033[m')\
        .replace('U', '\033[94mU\033[m')\
        .replace('V', '\033[93mV\033[m')\
        .replace('W', '\033[91mW\033[m')\
        .replace('X', '\033[92mX\033[m')\
        .replace('Y', '\033[91mY\033[m')\
        .replace('Z', '\033[94mZ\033[m')

def fibonacci(n):
    t1 = 0
    t2 = 1
    if n == 0:
        return 0
    else:
        for itr in range(n - 1):
            t3 = t1 + t2
            t1 = t2
            t2 = t3
    return t3