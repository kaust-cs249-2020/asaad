# 3.8 From Euler's Theorem to an Algorithm for Finding Eulerian Cycles
from Ex4 import Gnode
from Ex1 import listToString
def EulerCycle(graph):
    '''
    :params graph: a dict of nodes and edges
    '''
    # Fleury’s Algorithm 
    cycle = []
    stack = []
    visited = {}
    stack.append(list(graph.keys())[0])
    while len(stack) > 0:
        node = stack[-1]
        if graph.get(node):
            edge = graph[node][0]
            stack.append(edge)
            graph[node].remove(edge)
        else:
            cycle.append(stack.pop())
    if not graph.values():
        return []
    else:
        return list(reversed(cycle))


def constructGraph(paths):
    '''
    :params paths: node mappings from textfile  
    '''
    graph = {}
    for path in paths.split("\n"):
        path = path.split(" -> ")
        root = path[0]
        tonodes = path[1]
        tonodes = str(tonodes).replace("[", "").replace("]", "").replace("\'", "").replace("(", "").replace(")", "").split(",")
        graph[root] = tonodes
    return graph

if __name__ == "__main__":
    with open("Ex6.txt") as dataset:
        graph = constructGraph(dataset.read())
    print("->".join(EulerCycle(graph)))




