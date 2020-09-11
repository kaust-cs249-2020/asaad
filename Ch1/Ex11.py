#  1.8 Some Hidden Messages are More Elusive than Others 
from Ex7 import hammingDistance
from Ex4 import listToString
from Ex2 import MaxMap
from Ex10 import Neighbors
def FrequentWordsWithMismatches(Text, k, d):    
    # Input: A string Text as well as integers k and d. (You may assume k <= 12 and d <= 3.)
    # Output: All most frequent k-mers with up to d mismatches in Text.
    Patterns = list()
    freqMap = {}
    n = len(Text)
    for i in range(0, n-k):
        pattern = Text[i:i+k]
        neighborhood = list(Neighbors(pattern, d))
        for j in range(0, len(neighborhood)-1):
            neighbor = neighborhood[j]
            if neighbor not in freqMap.keys():
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] = freqMap.get(neighbor) + 1
    m = MaxMap(freqMap)
    for key in freqMap:
        if freqMap[key] == m:
            Patterns.append(key)
    return Patterns

if __name__ == "__main__":
    print(listToString(FrequentWordsWithMismatches("GGTAATATCTTAAATCTTGGTAGGTAATAAATTAAAGGTAATAATAAATTGGTAAATTAAAATAGGTAAAAATAGGTAATAAAAATAAATTAAAAATTATAATAAAAATATCTTTCTTATAATAAAAAAATCTTGGTATCTTTCTTAAAAATTAAAATAAATTAATTTCTTAAATCTTATAGGTAGGTAGGTAAATTAATTAAAAAAGGTAATATCTTAAAAAAAAAAAATCTTTCTTTCTTGGTATCTTTCTTAATTGGTATCTTATAGGTAATATCTTTCTTGGTAATAAAAAATTTCTTTCTTGGTAATAGGTAAATTAAAAATTAATTATAAATTAAATCTTGGTAGGTAATATCTTTCTTAAATCTTAATT", 6, 3)))
    