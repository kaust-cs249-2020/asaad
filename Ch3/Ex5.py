from Ex3 import suffix, prefix
# 3.5 Walking in the de Bruijn Graph
def construct_DeBruijnGraph(patterns):
    '''
    :params Text: a text string
    :params k: an integer k
    '''
    graph = {}
    for pattern in patterns:
        nodePrefix = prefix(pattern)
        nodeSuffix = suffix(pattern)
        if graph.get(nodePrefix):
            graph[nodePrefix].append(nodeSuffix)
        else:
            graph[nodePrefix] = [nodeSuffix]
    return graph    

def gprint(graph):
    for node in graph:
        if node.length() > 0:
            print(node)       

def dprint(degraph):
    for key in degraph:
        elements = str(degraph[key]).replace("[", "").replace("]", "").replace("\'", "").replace("(", "").replace(")", "")

        print(f"{key} -> {elements}")
if __name__ == "__main__":
    with open("ex5input.txt") as dataset:
        patterns = dataset.readlines()
    patterns = [x.strip() for x in patterns]    
    graph = construct_DeBruijnGraph(patterns) 
    dprint(graph)
    # for node in graph:
    #     if node.length() > 0:
    #         print(node)
