# 3.8 From Euler's Theorem to an Algorithm for Finding Eulerian Cycles
from Ex5 import construct_DeBruijnGraph
from Ex7 import EulerPath
from Ex2 import GenomePath
def StringReconstruction(patterns):
    dB = construct_DeBruijnGraph(patterns)
    path = EulerPath(dB)
    text = GenomePath(path)
    return text


if __name__ == "__main__":
    with open("Ex8.txt") as dataset:
        patterns = dataset.read().split("\n")
    print(StringReconstruction(patterns))
