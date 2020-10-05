#  4.6 A Branch-and-Bound Algorithm for Cyclopeptide Sequencing 
from Ex3 import CyclicSpectrum, constructAminoAcidMass, LinearSpectrum

aminoAcidMass = constructAminoAcidMass()

def expand(peptides):
    newPeptides = []
    for pep in peptides:
        for amino in aminoAcidMass.keys():
            newPeptides.append(pep + amino)
    return newPeptides


def mass(peptide):
    total = 0
    for pep in peptide:
        total += int(aminoAcidMass[pep])
    return total

def peptideToMass(peptide):
    mass = ""
    for i in range(len(peptide)):
        if i == len(peptide)-1:
            mass = mass + aminoAcidMass[peptide[i]]
        else:
            mass = mass + aminoAcidMass[peptide[i]] + "-"
    return mass

    
def CyclopeptideSequencing(Spectrum):
    candidatePeps = [""]
    Spectrum = [int(x) for x in Spectrum.split(" ")]
    finalPeps = []
    finalPepsMass = set()
    blacklist = []
    while len(candidatePeps) > 0:
        candidatePeps = expand(candidatePeps)
        # print(candidatePeps)
        for pep in candidatePeps[:]:
            # print(pep, mass(pep))
            if mass(pep) == max(Spectrum):
                if CyclicSpectrum(pep, aminoAcidMass) == Spectrum and (pep not in finalPeps):
                    finalPeps.append(pep)
                    finalPepsMass.add(peptideToMass(pep))
                candidatePeps.remove(pep)
            #     blacklist.append(pep)
            # elif not all(pepMass in LinearSpectrum(pep, aminoAcidMass) for pepMass in Spectrum):
            elif not all(pepMass in Spectrum for pepMass in LinearSpectrum(pep, aminoAcidMass)):
                candidatePeps.remove(pep)
                # print("removed", pep)
        # print(finalPeps)
        # blacklist.append(pep)
        # print(candidatePeps)
    return sorted(list(finalPepsMass))


if __name__ == "__main__":
    print(" ".join(CyclopeptideSequencing("0 103 128 128 129 129 131 131 137 163 234 240 258 259 259 260 266 291 291 362 369 371 388 389 395 419 422 422 498 499 500 517 525 526 550 550 551 628 629 629 653 654 662 679 680 681 757 757 760 784 790 791 808 810 817 888 888 913 919 920 920 921 939 945 1016 1042 1048 1048 1050 1050 1051 1051 1076 1179")))
                


