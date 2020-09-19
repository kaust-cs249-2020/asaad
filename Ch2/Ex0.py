#  2.2 Motif Finding Is More Difficult Than You Think 
import random as rand
def estimateProbablity(p, k, n, l):
    # input: probablity, k-mers, number of strings, length
    # output: probablity    
    freqMap = {}
    patterns = []
    for i in range(0, n):
        for j in range(0, l-k+1):
            pattern = ""
            for k in range(0, 9):
              pattern = pattern + rand.choice(list({"A", "T", "G", "C"})) # Since p = 25, we will just use choice function
            freqMap[pattern] = freqMap.get(pattern, 0) + 1
    maxValue = MaxMap(freqMap)
    print(maxValue)
    for key in freqMap:
        if(freqMap[key] == maxValue):
            patterns.append(key)
    return maxValue


def MaxMap(freqMap):
# Return the maximum value that exists in a dicitonary. Input: Dict {}, Output: Integer
    maxValue = 0
    for key in freqMap:
        if(maxValue < freqMap[key]):
            maxValue = freqMap[key]
    #print(maxValue) Debugging purposes 
    return maxValue


if __name__ == "__main__":
    sum = 0
    for i in range(0, 10000):
        sum = sum + estimateProbablity(0.25, 9, 500, 1000)
    print(sum/10000.0)