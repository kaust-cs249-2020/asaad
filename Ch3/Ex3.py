# 3.3 String Reconstruction as a Walk in the Overlap Graph

def prefix(text):
    return text[:-1]
def suffix(text):
    return text[1:]

class Gnode:
    def __init__(self, key, nodes):
        self.key = key
        self.nodes = nodes

    def get_key(self):
        return self.key
    def get(self, index):
        return nodes[index]
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
    def __repr__(self):
        return str([self.key, self.nodes])
    
        


def constructOverlapGraph(Patterns):
    '''
    :param Patterns: collection of k-mer patterns
    '''
    graph = []
    for pattern in Patterns:
        fnode = Gnode(pattern, [])
        graph.append(fnode)
    for Xnode in graph:
        for Ynode in graph:
            if(Xnode.get_key() != Ynode.get_key()):
                if(suffix(Xnode.get_key()) == prefix(Ynode.get_key())):
                    Xnode.add(Ynode)


        

        

    return graph

if __name__ == "__main__":
    with open("Ex3.txt") as dataset:
        patterns = dataset.readlines()
    patterns = [x.strip() for x in patterns]     
    graph = constructOverlapGraph(patterns)
    for node in graph:
        if node.length() > 0:
            print(node)
