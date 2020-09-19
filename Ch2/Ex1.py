# 2.2 Motif Finding Is More Difficult Than You Think
from Neighbors import Neighbors
from hammingDistance import hammingDistance
def MotifEnumeration(Dna, k, d):
    patterns = set()
    for word in Dna.split("\n"):
        for i in range(0, len(word)-k+1):
            pattern = word[i:i+k]
            neighborhood = Neighbors(pattern, d)
            for neighbor in neighborhood:
                found = False
                valid = True
                for string in Dna.split("\n"):
                    for j in range(0, len(string)-k+1):
                        if hammingDistance(neighbor, string[j:j+k]) <= d:
                            found = True
                    if not found:
                        valid = False
                    found = False
                        
                            
                if valid:
                    patterns.add(neighbor)

    return patterns

def approximateMatches(Pattern, Text, d):
    # Input: Strings Pattern and Text as well as an integer d.
    # Output: Countd(Text, Pattern).
    count = 0
    k = len(Pattern)
    for i in range(0, len(Text)-k+1):
        if(hammingDistance(Pattern, Text[i:i+k]) <= d):
            count = count + 1

    return count

if __name__ == "__main__":
    print(MotifEnumeration("AACCTCAGCCGATCGTCTGAGACTG\nGGACAGACTTGCCTGTACACCACCG\nAATCTGCGTTGTAACTACTAGACTG\nACGGCTCTCAATCGAGGCTGGCCAG\nTATTCTGGCGGACTGCACAGGACGT\nTCCACACGACGTACGGCCTGGCGCG", 5, 1))
