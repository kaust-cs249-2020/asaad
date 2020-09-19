# 2.5 Greedy Motif Search
def GreedyMotifSearch(Dna, k, t):
    bestMotifs = [x[0:k] for x in Dna.replace("\n", "")]
    motifs = []
    fString = Dna.split("\n")[0]
    for i in range(0, len(fString) - k + 1):
        motifs = []
        motif = fString[i:i+k]
        motifs.append(motif)
        for j in range(2, t):
            profile = constructProfile(motifs, k, t)
            motifs.append((profileMostProbable(Dna.split("\n")[j], k, profile)))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs

def constructProfile(motifs, k, t):
    # Use len(motifs) not t 
    size = len(motifs)
    profile = [[], [], [], []]
    for n in profile:
        for i in range(0, k):
            n.append(0)
    for motif in motifs:   
        for i in range(0, k):
            profile[0][i] = profile[0][i] + int(motif[i]=="A")
            profile[1][i] = profile[1][i] + int(motif[i]=="C")
            profile[2][i] = profile[2][i] + int(motif[i]=="G")
            profile[3][i] = profile[3][i] + int(motif[i]=="T")
    for n in profile:
        for i in range(0, k):
            n[i] = n[i]/(len(motifs)*1.0)
    # print(profile)
    return profile


def profileMostProbable(Text, k, profile):
    index = {"A": 0, "C":1, "G":2, "T":3}   
    maximumValue = 0
    mostprobablePattern = Text[0:k]
    for i in range(0, len(Text)-k+1):
        # AGCG
        pattern = Text[i:i+k]
        # print("Pattern", pattern)
        total = 1
        for j in range(0, k):
            # print("Letter of Pattern", pattern[j])
            total = total * profile[index[pattern[j]]][j]
        if maximumValue < total:
            maximumValue = total
            mostprobablePattern = pattern
    return mostprobablePattern

def listToString(indices):
    return str(indices).replace("[", '').replace("]", '').replace(",", '').replace("'","")

def score(motifs):
    total = 0
    if not motifs:
        return 0
    for i in range(0, len(motifs[0])):
        freq = {"A":0, "C":0, "G":0, "T":0}
        for j in range(0, len(motifs)):
            freq[motifs[j][i]] = freq.get(motifs[j][i], 0) + 1
            max_key = max(freq, key=freq.get)[0]
            total = total + (len(motifs) - freq[max_key])
    return total

if __name__ == "__main__":
    print(listToString(GreedyMotifSearch("GTTATATGTGTATCTAATGGGCGTATCGTATTTCTGACTGCTGTCCGGGGCATTGTCGTTCCTAAGTCAGGCCGCGGCCAGGTGAGGCATAAGCTGCAGACTATGCATGCAACCGGTGGTTAACCGTAGGGGAAAACGAAACACAGGTAGGGCAGT\nTTGATGTTTCACATATACGCGCCAAATGAAGATTTATCTCACTAGATCCCAACCGGTGCTCTAATTGTCTCTTTTCTAATCGCCATTGCTTGCGCGCGATGAACCTAGGACACTCGGATGCGGCGGACTACATAATCTCGGTTAGTACGTGGGTTC\nATGGTGTTAGATGGGACGCTGCATTGCTCTGTCGAGTGATCAGTACAACGACTCTAGGATGGAGGTCATCTATCAACAGGTCGTTCAGGTACTCATTTAAAATAGACGATTTCTGGTTTATCGCGCAACCATCACCCTGGTCGGGTTTCCGCTCTC\nGTAACTATGCCTTACCTGCGAAGGACGCATGACATTCTATATGCGCCCACAACCGGTGGTTTGCCAATTAGAGCTGGGACGCCGCTGTTACTCCGGCAGTACCTACCTAGGACCAGGTATATCCGACGATCCCAGCTATGTGGCATGATATGTGCG\nTGCAAGTATAGGGAAGCCTAATGTTCTCGGTGGAAAGTCGGCCGGTCTACATTCAATAAGTAAGCATGCTAATGCCTTCCCCATTTAGGGTTGACTGGACAACTCTAAACAACTGGTCATGAACGTTCGCAGTCAGGTTCCCGATTATTAGATACC\nCCTCCCTCAGCACTAACGGCCAGTCACCTTTTCGCTTCTTAGCACCTTCCACTTATCCGGAGGGAATGCAGGCTGGAACTCTCCTATCGAGCTGTCTTCATGCTTCAGGCCATAACTGTCGTTACATCGTAGCCAGATAGCCAGCCAACAGGTGTT\nCCAACAGGTGGTCTATCGGGTGTGATCCGGAGGGCCGTGCGCGAATAACGCCTGACGAGGACTTCTGTAACGCCTGCGCGGAACTGAATCCCTAGTGGCCGTGGGTCAATTACATTTAAGGCCCCGTGTCAGTACACCCGCACCCTGTCCCAGCGA\nATAATACGTGTTTGCAACGTTGGTACGTTGCGGAAAATTATGGTGTCAATAACGCATATCTAGTCATTCCGAAAATGATGGCATTGAGTGGTTGCTCTGACCATTCGCCCAACAGGTTATTTAACGGTCGACAGTCAGCCACACATGCCTCGTGAT\nACAACTGGTTTTACATTAATCTCAGGACCACTGACCGCATATTATACTACCTGGAAGAGATAAATGTTAGGGTCGACGAACCCACGTGGACACAGAGAACCTTGTTCTGTAAATTGAGTGCCGCTCTTGCCAAGCAAGTGTATTTAAGCCCAGACG\nCCCGTCCTGGCTCTGCGTCCCAAGCAGGGCAACCCTTATAGCATCTCAATCTGAAGAAGCCTTCTACGTACGAGCGGGCAGAACGTAGACGAAGGTTCAACGGGTCCTCTCCGCTCTAGACTTGAGCACGTACGTGTCGGCCCATGTACGCTGAAG\nGAGTTATCCTAGGGAGATCTTAGTTCCTCCGCCCAGACCAGGCGCACTCTATGTATGCCTATACCCAGGGTTATTCTTGCACTTTCGAAGTCAGTAACAACGGGTCGTAGCAGCCGGTAAGGTTGAGACTTAGTCCAAGACCAACGTTCTTTAGTC\nTAGAAATGCGGCAAGGACTGATCGATCTGACGAGGATTAGACTTTTTTTCTCGCGTCCTATTCTTTTGAGAAATGCAGGCACATTCAACAGGTATTCAGTATGTATGGCAATTTAATGCTGACAAGCCGTTGTCAGCACACAAGGCCTAGATATCG\nGTAGGTACCTTCAATCAAAGTAACTCACACTGCGACGGCACCTAGTCACCAACGGGTGCTAGATCCCGCTCGAATGGTGGTGAAGGAGGGGCACCACCTTTTTTTATCAAGTGAAAGTCTGGAGATGGAAAGATTACCCAATTGTCTCCGCCCCAC\nACGGATAGATCTCCGACATCGCCACATCCGAATAAGGCAACAGGTCGTCTGTTAAGGCTACCTACGGTCGAGACTGAATCATTGTTCCCATGCTTGGCGAGTTCAGGTGTGCCCTAAGGAGCGCAAATAATTGTAGCCAGAGCTGGAGTGACACCT\nCCAACAGGTTATCTTTTGATCACTAACTATAGTGAGTCAGAAGCGGAATAGATTATTACCACATCGCGGTCGGGCACTTAGTATGACTGCTGCTGGTAGACAAGAGAGATCTCCACATTTGAGGCATCGATACCCGGTATTGGTTGAGTGCTCCTC\nAGGTAGTTGGTACTGACACTCGGCACAACCGGTCTTGATTAGCCTACTTGCTAGCACACACTGCTAGTATGAGTTGAGACTACCGAGACCCCGCAGCCGCTTGAGTCATAAAGGGTAATGAGTATCTAGAGCACTGAGTGAGACCGTTCCGCTAGC\nAGGAGCTACTAAATACATATGTGAGAGCTAACTGCCACAACCGGTATTCCATGCCGCAGACCCGAACTTTGTGCGAATTGCCAATGTAGAGACGGATTTAAGGGATCTGTTCAGTGCACTGTGTCCGTCTATGGCGACTTTCGTGGAAGCCCGGCA\nTAAAGGAGGATACGCGACCGTGGTTATGATACTAGTAATCGCCTACTAGGCACTATCACGTGTATTAGCGGCATAGGCGTTATTACAATAGCACAAAGCCTTCGGGCGGCAACGGGTCCTTCTACATACCACATTTCATATATATCGTGTCATAAT\nGAGAGAATGCATGTTGCTGACTGTAATGGTAAAACTCGTGGCAACGGCGTATCATAGGATCTCACAAACAAGCCAGAGTTAACGTCAACGGGTAGTAGCCAATGAACTGCTTGTTTCCGTGGACGTTTAGGCGACTCCGCACCTAAAATGTATGAG\nACAACAGGTGTTACCTGTCGACTGGGGAATTGTGTTCATTCGGTATGGGTGTAAATAGTCATTGATTGTTGTTAGGTGCATTTGGAAGTCAGAATGTACCCGCCATAACATCCCGCATACAACTATAGGCGGGCTCGTTTTTTCTGAAGGTTGAGG\nTGACTGTAAGCTCCAGCTATGGGTTCAACTCACTACTCGCACTTGGAGGGTACGAGAGGAGTCTGGTTGCGGTGTAAGATCGTCCAGTTGCTGACATTGCGTGACGCTTGTGTAAGATGACGAGCAATTAGCGCAACGGGTGGTCATCGTGGAGGA\nCAGTCCTATCATGCGGGCATTAATCGGGTTTGGCCCAGAGATGAGAATTTGGTTAAACCTTTCAGTAACTGTTCAACCGGTTCTTAAATGTCCATAATCCTTACATCTCGGGGGCGATCCGCAGTACCTGCACTGGCTCTCCCGGTGTTCGATGTC\nAATAAGGGCGGTTACGCGGTGGTTATACTCAGGACCAGTCACGTGCGCGCTTAAAGGGAAACAACGGGTATTTGTAACAGATCTACTCCACCGTTTAGGAACGGGTTCACAGGTTATAGAGCGAGGCGGGTTATCGATAAAATTACAAGGCCAGCC\nTGAACGGGACTCGAAATTAGCCTAAGCAGTTGGGCGCATTAACGGTCGACACTCGACATGCACCTTTCGACAGACTGGTATAATCCGGTTCTAATTTGTGGACTTGAGCCAACTGGTGGTTTCTCAATTGATCATCCCAACACCCCTCGTGCGTTT\nCCAACAGGTCTTATCTTGACATATGGTTCGTTAATACGTGCGCGAGACCGTTCTGCATTCTCTTTCGGGAGACCGAGACGTAAGTGGAGGAACTAATTGACAGTTGTGAGCGTGCTAAAATACACTGGAGAGTTCACTATGGGCGCGGCGCGAGGA\nCGGAAGTTCCTCTGTCAGGTTTAGTAGCCACAGAGCATCCTTTCTTCTTATCAACGTCTTGTCAATAACGGCCATATCGGGTGATTCCTACATACACATTCTAAGACCTTATCGGCATCCATGGATTGACGGCGGTTTCAGAGTGCCAACCGCGCG\nAGGGACTCCGTTCTAGACTTTCATCAGCTACGGGCTGGAAACCGCAGACGCTTTCAGACTCCGGGGGCTCACAGGGCTTATGCGAAGTTCCCTATGCAGGCGAATGGATTGTTGGCAAGAATTTCAATCCGTAGGGCTTATCATAAGTCTTCCCTC\nTCCCGAAGCCCGGCTCGCTGTTGTTATTCAAGCAGCAAATAAATTACCAGCACTTGCCATGCCCGAATAATTATAAAACGCGGTAATATCAATCACGACACTACAGTGGTACCACGAGCCACAGACTGAAGACAAATTTTCGGCAGGTCTCAGATT\nATTAATGCGCTACGAGAATTCTCTAGATTTCAGAATTCTCATTCATGTCAGCAAGCCCGTTGTCGAGAGGTTTTAAATGCTACTCACCGCATCCCACCAGACTGTGCACCTAGATGTTAGCGCCCCCGGGGCATCACTTTATCAACGGTTGTCAAC\nTCGGGTCATCTTTGCAGTGTAGGGATAGGTCCTGTTTGGATCTATGTATGAAGGGATACCTCTAGTAGTTCTCAGGGCCCGCCCGCACCACTGGGAGCAGGGGTTGATCGACTCGTGTAGGGGTATCAGATTACCAGGGGATGAGTGTAGGATATT\nGGAAAAGATTCTTAGCGTCTTGCATCGGGACCTGGGGCGGCTCCAGAGCCACACTGTCATTCGGACAGTTCCAGTTTTCAGAGTTTATTAGTGCAGTATGTAAACCCGATATATGACAGCCCAAAACCATAGCTAGTCGTCTCCGGCACGGTCCTG\nTTCGGCGCACGTCCTAATCCTTCTGCAAAACGATTTCCAAAAATCCTTACGAGGCTACCAAGAAGACTCCAGAAAACAAGGTTTGGTTATCAGACTCCTGACCGAGACGTGCCACACATTTCCTGGATTGTATGTTTCAACGCGTGAGGGGTATAT\nATCACCTCGAACCTGATCTGGTCACCTCCGCGGGGACGGGTTTCCACAGTGCAACCTTCCGAGTTATCCTGCTGTCTGTGACCGTGATGTCAGAATACACGCGTAATTTTGACCTCGCATGTGGGAGCAAACGTACCGTGGTGCAAACTTTGACAC\nCGATTTCAGAGTATGAACGTGTATGCATGTACAGACTCGCATCAAATCGCAGGGAAGTTGAGAGATTAGTACAGTTCCAACCTGACGCCACTGTTAGATAACTGAGGAGTAGCTCGGGTGTCGCCCCAACAAGGTAATAACACGGTTGCAGCGCCT\nGTACTATATATGCTTGGCATCCATTTCAGAATGCCAAGGCCTCGGAGTGGCGAACGTTCTAGGTGTGTTCAATGCAACTATACCTCGCGTTTGTAATGGTCTCAGAGTTAGCATGACCTCACGTAAGCTACTAAGCTGAGACATCCGAGGCAAATA\nGAGATTCCTGGTCCCTCCAAATCGACAGCCGCGCGACTGCACTGACTCTCGGGAGGGGGTGGTCGGATTTCACTAACGCCGATTGTGGGAGTGCTCTTAAAACTGAGGCGATTTCAGACTAATTGTGGGGTTGGCACGACCGGATAGCGGGTGAAC\nCGTTTTGACATTGTATTGTACAGAGGCGACTGCTAGTAGCATTTACTCTCCGCACAATGCGCCGTTAAACTAGCGTATTTTTACTCACCGCGATTGGTGGACCGAGCGGGATTTCAGAGTTTACGCATTTCTGCGAGGGCATCTCGTAATCATAAA\nAGAACGTGCCGCTGCTGGCGGTGCCAACAGAGCTGATGGGCACACTCTCGGATCGATCTATGTCAACCGGAGCATCAATACCGGAGTTCGGATAAACTAGTCGACACGTGATTTCAGACTCCCAAGTCACCGGAACTACTGCGAGACTTTGTTTTC\nGTAGATCCTGCATTACCTCCGTCAGGACGCCTCAACCTAACGTAAGCTGAGAGGCTCCTACACTTAGGAAAAGGGTTTCAGACTGGGTAGGATGTGAAGCTTATTATTGGCAAAATCAAACACCGAGAGGATGACCCTAAGGGGTTGAGAGTATTT\nTCTGCAAAACTTCGGTCCCGCTATGGTCAGCGAACAGGTGCCTCTTAATATCTCATCGGGTTTGCCACGCTTAGCCCACTTTCACAGCACATTTGTAGCTTTCAGAGTTTGTCACTCGGATACGGGACAGCGCTGATAGTTTCCATGCGCGCGAAA\nAGTTTTCAGAATTGAAAACGCACGTGAAGTGTGTGACTCCGTTGAGGAGGATCTTTAGTGAACCCATGATAGTATGATAGGTCTCATTCTCTCCGTACAACTCAGGAATCAACTAAGCTACTGCTTGCGTCTGTCTGTAGGCTAAAAGCCAGGGAC\nATATCCTCCAGGATTCAAAATCCCGCCTGATAGCGCCGGTAACATACAGGGTATCAGATTTGCACCTGAGGTGGCTCGAGCGGTGACTTCGGGTATGGGCCAACAGGAATAGGGATGACACCAATCAAATTATTGTGGAAGCTCGGCTGCCAACTG\nGTACTCACCCTCCTTCCGAGTCGATCCGTTTGCATTGTAGGTCCAATTCCCCCCCTTCTGCCGCAGCCCATCTGATCCAATTGACCTAATACGTCGTTTGCCACTCAAGTAAGTACACTAAGCTATCAGATTGCACCGCTTATTTCTCTGCGAACC\nACAGATTAGTTGTGATATCAGATTCGAGTATCAGCCAAGTGGTCCGCATAACACAGCTATAGCGTTTCATTCTAAACTTAAACATCGAGGCTTTCCATACGGGTAATCAGCGAGCAGTAATGGGGTTTAGTCTGCCGACCTATGCACTGGATAACC\nAAGACCAACTCACTGATGCCGGTTTCCCGCGTTGCAGTCCGGAAGAAATTGTATGGCTCAGGGAGAGTAGTATAATCATGAGATAGCCCTGTACAGCCTGGTGCGCGATGTTTTCAGAATCTGGGGTTTGGCCCATCTCTTTCTGGGGCAAGGTTG\nTTCCTAGGTATGCTTGGACACACATATATCAAAGGCGGACTAGTCTTGTGCCCCTCTTAGACTTGCGCACGTGGGTTTCAGATTATCAATAGTGCACAATGATAACAAGAGCTTGGGTGTGGATCTACAAGCTACCATATCCTCAGCTGCAAAGCC\nCCCTGTATAGTCGAGAGACCCCACTAATGATCATGACTATGCAATTCAGTCTGATCGTGCGCAATTTCCATGCGGTATCAGACTTCTGCTAGAGGAAAAGCATGAGATTCGAGAGCCTAGTGCCACAAGATTCGTTTGTGGCTTCGCACAAGGATG\nCGTGTCGTGTTACAACATGCTAACAATCATGAGCACCATGTGTGTCCCTTAGGCAGATCTCGGCCCGCCTTATCCTAGCTGCAAGACAGTGTCGCAACTATCATGCGAGGATTTCAGATTATTGGAACTCGAAGTTTCTAGCGAGGAACCATCCAC\nCACGAGTGCTTCGGTTTTCAGACTTAGGTTTAAAAGTTCTGGTGGAGTTCCGCGGGGCCGCGCATAGATAGACGATTTGCCTACTCGGATGAACTAGCATGCGCCGTCGCTACTCCCCGATCTTTTGTATAATAATAAAAGTCTCTCATCTCAAGA", 12, 25)))
    # print(greedy_motif_search(["GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"], 3, 5))
    # profile = constructProfile(["CAG", "CAG", "CAA", "CAA", "CAA"], 3, 5)
    # print(profile)
    # print(profileMostProbable("CAATAATATTCG", 3, profile))