# 1.8 Some Hidden Messages are More Elusive than Others
# Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
from Ex7 import hammingDistance
from Ex4 import listToString

def approximateMatches(Pattern, Text, d):
    # Input: Strings Pattern and Text along with an integer d.
    # Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
    positions = list()
    k = len(Pattern)
    for i in range(0, len(Text)-k+1):
        if(hammingDistance(Pattern, Text[i:i+k]) <= d):
            positions.append(i)

    return listToString(positions)

if __name__ == "__main__":
    print(approximateMatches("AAAAA", "AACAAGCTGATAAACATTTAAAGAG", 2))
        