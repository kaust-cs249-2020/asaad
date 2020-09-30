#  3.3 String Reconstruction as a Walk in the Overlap Graph

def GenomePath(Path):
    '''
    :param Path: A sequence path of k-mers 
    '''
    text = ""
    prev = ""
    k = len(Path[0])
    for pattern in Path:
        if(not prev):
            prev = pattern
            text = text + pattern
        else:
            if(prev[1:] == pattern[:k-1]):
                prev = pattern
                text = text + pattern[-1]
    
    return text

if __name__ == "__main__":
        with open("dataset_369268_3.txt") as dataset:
            path = dataset.readlines()
        path = [x.strip() for x in path] 
        print(GenomePath(path))