#  1.2 Hidden Messages in the Replication Origin 
def frequencyTable(Text, k):
    # Input: A string Text and an integer k.
    # Output: All most frequent k-mers in Text.
    freqMap = {}
    for i in range(0, len(Text)-k):
        pattern = Text[i:(i+k)]
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] = freqMap.get(pattern, 1)+1
    return freqMap



def MaxMap(freqMap):
# Return the maximum value that exists in a dicitonary. Input: Dict {}, Output: Integer
    maxValue = 0
    for key in freqMap:
        if(maxValue < freqMap[key]):
            maxValue = freqMap[key]
    #print(maxValue) Debugging purposes 
    return maxValue

def betterFrequentWords(Text, k):
# Return the most frequent words in Text, Input: Text, k-mers, Output: frequent string patterns
    frequentPatterns = list()
    freqMap = frequencyTable(Text, k)
    maximumFrequency = MaxMap(freqMap)
    for freqPattern in freqMap:
        if(freqMap[freqPattern] == maximumFrequency):
            frequentPatterns.append(freqPattern)
    return frequentPatterns

if __name__ == "__main__":
    print(betterFrequentWords("ACAGGATACAGGATATCCTGACGCAGTCGAAGCAGTCGAAGCAGTCGAAGCTGAAGGCTGAAGGATCCTGACGATCCTGACGATCCTGACGCAGTCGAAGACAGGATATCCTGACGACAGGATACAGGATACAGGATAACTCCAATCCTGACGCAGTCGAAGATCCTGACGCTGAAGGAACTCCACTGAAGGACAGGATCTGAAGGACAGGATACAGGATATCCTGACGCAGTCGAAGCAGTCGAAGAACTCCAATCCTGACGATCCTGACGCAGTCGAAGACAGGATCAGTCGAAGCAGTCGAAGCTGAAGGAACTCCAAACTCCACAGTCGAAGAACTCCAACAGGATCTGAAGGACAGGATATCCTGACGATCCTGACGCTGAAGGACAGGATCTGAAGGATCCTGACGCTGAAGGCAGTCGAAGAACTCCAATCCTGACGACAGGATCTGAAGGCTGAAGGACAGGATACAGGATACAGGATACAGGATATCCTGACGCTGAAGGATCCTGACGATCCTGACGAACTCCACAGTCGAAGCAGTCGAAGACAGGATCAGTCGAAGCAGTCGAAGACAGGATAACTCCACTGAAGGATCCTGACGAACTCCAAACTCCAATCCTGACGCTGAAGGCTGAAGGCTGAAGGAACTCCACAGTCGAAGCTGAAGGCAGTCGAAGCAGTCGAAGATCCTGACGATCCTGACGATCCTGACGACAGGATCTGAAGGAACTCCAAACTCCAATCCTGACGCAGTCGAAGCTGAAGGCTGAAGGCTGAAGGACAGGATCTGAAGGACAGGAT", 11))

    