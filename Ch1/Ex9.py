# 1.8 Some Hidden Messages are More Elusive than Others
# Approximate Pattern Count Problem: Find all approximate counts of a pattern in a string.
from Ex7 import hammingDistance
from Ex4 import listToString

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
    print(approximateMatches("TTTAGAGCCTTCAGAGG", "GAGCTTACAGCCGTGTATGCAGTGTTTCGTTGTGATAATCGTTGAACGAGCCATGGATGGAACACGCGGGAATTGCACAGATAATTTCTATAAGAGGATATGCTCTGGGAGTTTCCAGCGTTCGATTATCCCCTTGTAAAATCGCAAGGTCCGTGGCAGTATAAGCCAACAAATATAGGAGTTGTACCTGAACCGAGCCAATGAGTGCCTAATGAGACCATTTTTAGCAATCTATCTGTTCTCCGAAGTGGGTACAAGACGGGACAGCACCTGCATCTGCCGTCGGGGTGCAGGCCCTTGAAGATGTGAGGGATCATCCTGGATTTGGTCCACCCTTACAGGCCTTTAGTCAATAAAGGCGG", 3))
        