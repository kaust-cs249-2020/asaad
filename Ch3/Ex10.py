#  3.9 Assembling Genomes from Read-Pairs
from Ex3 import suffix, prefix
from Ex7 import EulerPath

def construct_DeBruijnGraph_Pairs(pairs):
    '''
    :params Text: a text string
    :params k: an integer k
    '''
    graph = {}
    for pair in pairs:
        nodePrefix = (prefix(pair[0]), prefix(pair[1]))
        nodeSuffix = (suffix(pair[0]), suffix(pair[1]))
        if graph.get(nodePrefix):
            graph[nodePrefix].append(nodeSuffix)
        else:
            graph[nodePrefix] = [nodeSuffix]
    return graph    

def genomePath_pairs(k, d, pairs):
    '''
    :param gapped_patterns: the sequence of (k, d)-mer pairs 
    :param k: k-mers length
    :param d: the distance between the pair
    :return: a string of length (2k + d + n -1), such that the i-th (k, d)-mer = (ai,bi) for i between 1 and n
    '''
    prefString = ""
    suffString = ""
    for i, (p1, p2) in enumerate(pairs):
        if(i == 0):
            prefString = prefString + p1
            suffString = suffString + p2
        else:
            prefString = prefString + suffix(p1)[-1]
            suffString = suffString + suffix(p2)[-1]
    for i in range(k + d + 1, len(prefString)):
        if prefString[i] != suffString[i-k-d]:
            return "There is no string spelled by the gapped patterns"
    return prefString + suffString[-(k+d):]
    


def StringReconstruction_Pairs(k, d, pairs):
    for i, pair in enumerate(pairs):
        pair = pair.split("|")
        pairs[i] = pair
    graph = construct_DeBruijnGraph_Pairs(pairs)
    path = EulerPath(graph)
    text = genomePath_pairs(k, d, path)
    print(text)

if __name__ == "__main__":
    with open("challenge.txt") as dataset:
        pairs = dataset.read()
        StringReconstruction_Pairs(120, 1000, pairs.split("\n"))


