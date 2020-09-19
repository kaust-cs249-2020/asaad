# 2.5 Greedy Motif Search
def profileMostProbable(Text, k, profile):
    index = {"A": 0, "C":1, "G":2, "T":3}
    maximumValue = 0
    mostprobablePattern = ""
    for i in range(0, len(Text)-k+1):
        # AGCG
        pattern = Text[i:i+k]
        total = 0
        for j in range(0, k):
            if total == 0 and j == 0:
                total = profile[int(index[pattern[j]])][j]
            else: 
                total = total * profile[int(index[pattern[j]])][j]
        if maximumValue < total:
            maximumValue = total
            mostprobablePattern = pattern
    return mostprobablePattern

if __name__ == "__main__":
    print(profileMostProbable("TTCCGGCTAGGCGCACCTAATTTTTCTGTGTCGTGCTCGTTGGTGAGTTCTCTATTAACTCGCTTTATTGCACGGTGTGCGTGGTGTTACGCATATAGCCATATCTTATTCGTCCCATACGGGGGCCAAGTAGCATCAAGCGCGTGTGAGGAAGCAAGCAATAGTTAAGAACGTCCAACCTTTGTACCGGTGCGCTCATTGCGGTCGGCCATTGCAACAGGGGTGATATGATACCTTTGATTCGGCCTCTGAAGGCCGTTACGCTTTAGCTGTCTACGCTACTCTTCTAGGCTGGTTAGCACCCTCACAAGATCAATTGGTAGTGGGCTTCCTTTGCTTTTCGAGTCTCGAGAGACCGGTGACCACGAGTCATACTATCGGCGGAGAATTAGGCGTCAAGACGCGCCTGAAACTGCCTTATGGGTGACCTATGATATACACACGGTTCCAAATCTAGCGTCGTAATGGAGACCTTCCATAGTCCGGTCAACAGCATGTAAGGTTCGTGATTCCAGCGAAGGCCAGCGGTATATCCAGCATTATGCTGCTAAGGTTAGAATCGACGAGAGCAATACACCGCGCCCCGGTAGGTGCGTCGCTCGTAATCCGACGGTTCGCGGGGCAAGAGCATGCGGCCAAAAACTACGCTGGTCCGCCACGAATTCAATGCGTACAGAGTTACTAGCCTGTATTCGCCCCCTGAATCTATCATGGGATGGATATAATAACTTACACGCCTGCTGATCAACTACTAGTTACGGATGGGTTATGAAAATATAACTGTGGACAATCACATGAATTTTAAGCAGGTTCTATGAAATACTTTCGACCTAATCTAGAAGGGTCTCTGAAAAATAGTAAGTAGCAACGCAAGGGCGTACACGTTATATATTAGCATTTACCTTTGAGAGCGGCCGCTTCCCATCATGAGTGAATGGGCTGTGATAGAGTAGCAGTACCCGATGTTTTGTTATCAATGCATGCAGTGCGCGACTAGGCC", 13, [[0.289, 0.237, 0.237, 0.303, 0.224, 0.25, 0.132, 0.25, 0.237, 0.237, 0.276, 0.224, 0.184], [0.276, 0.25, 0.211, 0.276, 0.289, 0.303, 0.25, 0.237, 0.25, 0.184, 0.316, 0.276, 0.316], [0.303, 0.263, 0.382, 0.211, 0.224, 0.184, 0.276, 0.237, 0.263, 0.316, 0.132, 0.224, 0.224], [0.132, 0.25, 0.171, 0.211, 0.263, 0.263, 0.342, 0.276, 0.25, 0.263, 0.276, 0.276, 0.276]]))
