#1.7 Peculiar Statistics of the Forward and Reverse Half-Strands
# Minimum Skew Problem: Find a position in a genome where the skew diagram attains a minimum.
from Ex4 import listToString

def minimumSkew(Genome):
    # Input: A DNA string Genome.
    # Output: All integer(s) i minimizing Skewi (Genome) among all values of i (from 0 to |Genome|)
    minVal = 999 # Is it best to start from 0?
    skewness = 0
    positions = list()
    skewValues = {"G": 1, "C": -1, "A": 0, "T": 0, "g": 1, "c": -1, "a": 0, "t": 0}

    for i in range(0, len(Genome)):
        skewness = skewness + skewValues.get(Genome[i])
        if(minVal > skewness):
            positions = list()
            minVal = skewness
        if (minVal == skewness):
            positions.append(i+1)

    return (skewness, positions)

if __name__ == "__main__":
    with open('dataset_369238_6.txt', 'r') as file:
        data = file.read().replace("\n", "")
        print(listToString(minimumSkew(data)[1]))

