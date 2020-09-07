
import random
    
def decipher(code):
    countDict = {}
    print(code)
    for c in code:
        countDict[c] = countDict.get(c,0)+1
    

    freqSort = sorted(countDict, key=countDict.get, reverse=True)
    print(freqSort)
    freqSort.remove("E")
    freqSort.remove("T")
    freqSort.remove("H")
    while True:
        rcode = code
        frequencyAlphabet = list("BSCYROUFWA")
        random.shuffle(frequencyAlphabet)
        frequencyAlphabet = ''.join(frequencyAlphabet)
        print(frequencyAlphabet)
        count = 0
        for letter in frequencyAlphabet:
            
            rcode = rcode.replace(freqSort[count], letter)
            count = count + 1
        if("AGOOD" in rcode):
            break
        print(rcode)



if __name__ == "__main__":
    decipher("53zzx305))6yTHE26)Hz.)Hz)TE06yTHExE^60))E5T161T:zyE\
xE3(EE)5yxTH6(TEEy96y?TE)yz(THE5)T5yx2:yz(TH956y2(5\
ywH)E^EyTH0692E5)T)6xE)HzzT1(z9THE0E1TE:Ez1THExE5TH\
)HE5x52EE06yE1(z9THET(EETH(z?3HTHE)HzT1z(T:1EETz?T")


