#  1.3 Some Hidden Messages are More Surprising than Others 
def indexOfPattern(Pattern, Genome):
    # Input: Two strings, Pattern and Genome.
    # Output: A collection of space-separated integers specifying all starting positions where Pattern appears as a substring of Genome.
    k = len(Pattern)
    indices = list()
    for i in range(0, len(Genome)-k):
        if(Genome[i:(i+k)] == Pattern):
            indices.append(i)
    return listToString(indices)

def listToString(indices):
    return str(indices).replace("[", '').replace("]", '').replace(",", '').replace("'","")

if __name__ == "__main__":
    with open('Vibrio_cholerae.txt', 'r') as file:
        data = file.read().replace("\n", "")
        print(indexOfPattern("ATGATCAAG", data))
