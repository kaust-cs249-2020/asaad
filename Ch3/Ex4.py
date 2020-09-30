from Ex3 import suffix, prefix
# 3.4 Another Graph for String Reconstruction
class Gnode:
    def __init__(self, key, nodes):
        self.key = key
        self.nodes = nodes

    def get_key(self):
        return self.key
    def get(self, index):
        return nodes[index]
    def get_edges(self):
        return self.nodes
    def __getitem__(self, index):
        return 
    def length(self):
        return len(self.nodes)
    def add(self, node):
        self.nodes.append(node)
    def __str__(self):
        string = f"{self.key} -> "
        for i in range(0, len(self.nodes)):
            if(i == len(self.nodes)-1):
                string = string + self.nodes[i].get_key()
            else:
                string = string + self.nodes[i].get_key() +", "
        return string
    def __eq__(self, other):
        return self.get_key() == other.get_key()
    def __hash__(self):
        return hash(self.get_key())
    def __repr__(self):
        return str([self.key, self.nodes])

def construct_DeBruijnGraph(Text, k):
    '''
    :params Text: a text string
    :params k: an integer k
    '''
    graph = {}
    n = len(Text)
    patterns = []
    for i in range(n-k+1):
        pattern = Text[i:i+k]
        patterns.append(pattern)
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
    graph = construct_DeBruijnGraph("AAGATTCTCTAAGA", 4)
    dprint(graph)
    # for node in graph:
    #     if node.length() > 0:
    #         print(node)
