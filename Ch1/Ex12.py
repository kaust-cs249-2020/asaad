#  1.8 Some Hidden Messages are More Elusive than Others
from Ex7 import hammingDistance
from Ex4 import listToString
from Ex2 import MaxMap
from Ex10 import Neighbors
from Ex3 import reverseComplement
def FrequentWordsWithMismatchesAndRC(Text, k, d):
    # Input: A DNA string Text as well as integers k and d.
    # Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern)+ Countd(Text, Patternrc) over all possible k-mers.
    Patterns = list()
    freqMap = {}
    n = len(Text)
    for i in range(0, (n-k+1)):
        pattern = Text[i:i+k]
        rcpattern = reverseComplement(pattern)
        neighborhood = list(Neighbors(pattern, d)) 
        neighborhoodr = list(Neighbors(rcpattern, d)) # Reem Alternative: Apply RC to each original Neighborhood (Improves Space Complexity)

        for j in range(0, len(neighborhood)):
            neighbor = neighborhood[j]      
            neighborR = neighborhoodr[j]
    
            freqMap[neighbor] = freqMap.get(neighbor, 0) + 1
            freqMap[neighborR] = freqMap.get(neighborR, 0) + 1
    maxValue = MaxMap(freqMap)
    for key in freqMap:
        if freqMap[key] == maxValue:
            Patterns.append(key)
    return Patterns

if __name__ == "__main__":
    print(listToString(FrequentWordsWithMismatchesAndRC("GATTGAGAAGTTGAGAAGTTGAGAAGAGTAGATATTGAGAGAGAACGAGAACACTAGATTTAAGTAGATAAGTTACACGATTAGGAACACTTTATTGATTGAACAGGATAACTATAAGTTGAACACTTTTTTAGTATTTTTATAACACGATATTACTATAGATTACGATAAGTATAACGATTTAACACGAGATTACGAACTTAG", 5, 3)))
    