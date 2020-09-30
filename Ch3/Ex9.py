from Ex8 import StringReconstruction
from Ex5 import construct_DeBruijnGraph
from Ex6 import EulerCycle
from Ex2 import GenomePath
def k_UniversalString(k):
    patterns = []
    for i in range(2 ** k):
        patterns.append(f'{i:0{k}b}')
    dB = construct_DeBruijnGraph(patterns)
    cycle = EulerCycle(dB)[:-(k-1)]
    text = GenomePath(cycle)
    
    return text

if __name__ == "__main__":
    print(k_UniversalString(4))