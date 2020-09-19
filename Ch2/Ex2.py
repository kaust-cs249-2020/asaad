#  2.4 From Motif Finding to Finding a Median String 
from hammingDistance import hammingDistance
def MedianString(Dna, k):
    text = Dna.replace("\n", "")
    median = ""
    distance = 9999
    for i in range(0, len(text)-k+1):
        pattern = text[i:i+k]
        # print(pattern)
        if distance > d(Dna, pattern):
            distance = d(Dna, pattern)
            median = pattern
    return median

def d(Dna, pattern):
    k = len(pattern)
    total = 0
    for seq in Dna.split("\n"):
        minValue = 99999
        for i in range(0, len(seq)-k+1):
            subsequence = seq[i:i+k]
            minValue = min(minValue, hammingDistance(pattern, subsequence))
        total = total + minValue
        # print(total)
    return total

if __name__ == "__main__":
    print(MedianString("CGCTCTAGCGATCATCCCTTGCTAGGATTCTACAGAGTCCAC\nAGTGCGTTATTCAGCAACTCTAATAAATTTTCGCGACATCCA\nATGTTGTCGGTGGAAGGGCTATGTGTAGTCCATCCAGGGTAG\nCATCCTTCTATGCTCCGGTAGTATCTCCCGGCATCTATCTAT\nCCTGTCCCTGTTGCAGAGTCCTTCCATCCACAGGTAATCTGT\nGGGTATGGCGGTGAATGAACCTGCCATCCGTTGTTTGGAAAA\nTAGAAATCGAACGGTGACCATCCGGGGCGACGATCCAGAGGC\nTGTTCAGGGTGGTCGTTCCTCTCACGGTTCCATCCAGGTCCC\nTAGGCACTCAGGGGGTACAAGACTCTGAAACATCCAAAGCTC\nCTGAGTGCGTACAGCCTGGGCTGCTTCTACCATCCAGTCTTA", 6))
