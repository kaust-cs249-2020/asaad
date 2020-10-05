# 4.9 The Spectral Convolution Saves the Day 
from Ex5 import score, mass, peptideToMass, trim
from Ex3 import CyclicSpectrum, constructAminoAcidMass, LinearSpectrum
aminoAcidMass = constructAminoAcidMass()

def spectral_convolution(spectrum):
    conv_spectrum = []
    if type(spectrum) != list:
        spectrum = [int(x) for x in spectrum.split(" ")]
    for e1 in spectrum:
        for e2 in spectrum:
            difference = e2 - e1
            if difference > 0:
                conv_spectrum.append(difference)
    return conv_spectrum

def expand(peptides, convoList):
    newPeptides = []
    for pep in peptides:
        for amino, mass in aminoAcidMass.items():
            if int(mass) in convoList:
                newPeptides.append(pep + amino)
    return newPeptides

def count_convolution(spectrum):
    conv_count = {}
    convolution = [int(x) for x in spectral_convolution(spectrum)]
    for diff in convolution:
        if 57 <= diff <= 200:
            conv_count[diff] = conv_count.get(diff, 0) + 1
    conv_count = sorted(conv_count.items(), key=lambda item: item[1], reverse=True)
    return conv_count



def ConvolutionCyclopeptideSequencing(spectrum, m, n):
    count_conv = count_convolution(spectrum)
    convolution = []
    maximumValue = 0
    for i, pair in enumerate(count_conv):
        if i < m:
            print(pair)
            convolution.append(pair[0])
            maximumValue = pair[1]
        elif i>=m and pair[1] == maximumValue:
            convolution.append(pair[0])
    return LeaderboardCyclopeptideSequencing(spectrum, n, convolution)



def LeaderboardCyclopeptideSequencing(Spectrum, N, convolution):
    leaderBoard = [""]
    Spectrum = [int(x) for x in Spectrum.split(" ")]
    leaderPeptide = ""
    while len(leaderBoard) > 0:
        leaderBoard = expand(leaderBoard, convolution)
        # print(leaderBoard)
        for pep in leaderBoard[:]:
            # print(pep, mass(pep))
            if mass(pep) == max(Spectrum):
                if score(pep, Spectrum) > score(leaderPeptide, Spectrum):
                    leaderPeptide = pep
            elif mass(pep) > max(Spectrum):
                leaderBoard.remove(pep)
        leaderBoard = trim(leaderBoard, Spectrum, N)
                # print("removed", pep)
        # print(finalPeps)
        # blacklist.append(pep)
        # print(candidatePeps)
    return peptideToMass(leaderPeptide)

if __name__ == "__main__":
    print("-".join(ConvolutionCyclopeptideSequencing("0 57 57 71 71 103 113 114 115 128 128 129 147 156 163 171 185 200 204 218 227 229 242 242 260 266 275 286 299 313 317 319 332 332 356 357 381 388 389 389 390 414 422 445 446 446 460 460 469 493 495 517 517 517 519 537 552 559 561 574 588 608 616 622 623 632 645 651 664 673 674 680 688 708 722 735 737 744 759 777 779 779 779 801 803 827 836 836 850 850 851 874 882 906 907 907 908 915 939 940 964 964 977 979 983 997 1010 1021 1030 1036 1054 1054 1067 1069 1078 1092 1096 1111 1125 1133 1140 1149 1167 1168 1168 1181 1182 1183 1193 1225 1225 1239 1239 1296", 19, 331)))
