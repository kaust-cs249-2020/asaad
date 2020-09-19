#  1.11 CS: Generating the Neighborhood of a String 
from hammingDistance import hammingDistance
from indexOfPattern import listToString
def Neighbors(Pattern, d):
    
    # Input: A string Pattern and an integer d.
    # Output: The collection of strings Neighbors(Pattern, d).
    if d == 0:
        return {Pattern}
    if len(Pattern) == 1:
        return {"A", "C", "G", "T"}
    Neighborhood = list()
    suffixNeighbors =  Neighbors(Pattern[1:], d)
    for text in suffixNeighbors:
        if hammingDistance(Pattern[1:], text) <= d:
            for x in {"A", "C", "G", "T"}:
                Neighborhood.append((x+text))
        else:
            Neighborhood.append((Pattern[0]+text))

    return Neighborhood

if __name__ == "__main__":
    print(listToString(list(Neighbors("CATCGATGCC", 2))))


