# 3.10 Epilogue: Genome Assembly Faces Real Sequencing Data
from Ex5 import construct_DeBruijnGraph
from Ex1 import listToString

def graph_degrees(graph):
    balance = {}
    for key in graph.keys():
        edges = graph[key]
        if key in balance:
            balance[key][1] = len(edges)           
        else:
            balance[key] = [0, len(edges)]
        for e in edges:
            if e in balance:
                balance[e][0] = balance.get(e)[0] + 1
            else:
                balance[e] = [1, 0]
    return balance

def maximal_branching(graph):
    paths = []
    degrees = graph_degrees(graph)
    for node in graph:
        if degrees[node] == [1, 1]:
            nextNode = graph[node][0]
            last = len(nextNode) - 1
            if nextNode in graph:
                if node == graph[nextNode][0]:
                    isolatedCycle = [node]
                    while nextNode != node:
                        isolatedCycle.append(nextNode[last])
                        if nextNode in graph:
                            nextNode = graph[nextNode][0]
                        else:
                            break
                    isolatedCycle.append(nextNode[last])
                    # print(isolatedCycle)
                    paths.append(''.join(isolatedCycle))
                else:
                    break
        else: 
            for child in graph[node]:
                nonBranching = [node]
                nextNode = child
                last = len(nextNode) - 1
                while True:
                    nonBranching.append(nextNode[last])
                    degree = degrees[nextNode]
                    if degree == [1, 1]:
                        nextNode = graph[nextNode][0]
                    else:
                        break
                    # print(nonBranching)
                paths.append(''.join(nonBranching))
    return sorted(paths)

def contig_generation(patterns):
    graph = construct_DeBruijnGraph(patterns)
    maximal_branches = maximal_branching(graph)
    return maximal_branches

if __name__ == "__main__":
    with open("Ex11.txt") as dataset:
        patterns = dataset.read().split("\n")
    print(listToString(contig_generation(patterns)))
