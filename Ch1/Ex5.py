# 1.4 An Explosion of Hidden Messages 
from Ex2 import frequencyTable
from Ex4 import listToString
# Solve the Clump Finding Problem 
def findClumps(Text, k, L, t):
    # Input: A string Genome, and integers k, L, and t.
    # Output: All distinct k-mers forming (L, t)-clumps in Genome.
    patterns = set()
    for i in range(0, len(Text)-L):
        textWindow = Text[i:i+L]
        freqMap = frequencyTable(textWindow, k)
        for key in freqMap:
            if freqMap.get(key) >= t:
                patterns.add(key)
    return listToString(list(patterns))


if __name__ == "__main__":
    with open('E_coli.txt', 'r') as file:
        data = file.read().replace("\n", "")
        print(findClumps(data, 9, 500, 3))