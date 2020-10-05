# 4.11 CS: Generating the Theoretical Spectrum of a Peptide

def LinearSpectrum(Peptide, AminoAcidMass):
    prefixMass = [0]*(len(Peptide)+1)
    for i in range(1, len(prefixMass)):
        if(Peptide[i-1] == "L"):
            peptideMass = int(AminoAcidMass["I"])
        elif(Peptide[i-1] == "Q"):
            peptideMass = int(AminoAcidMass["K"])
        else:
            peptideMass = int(AminoAcidMass[Peptide[i-1]])
        prefixMass[i] = (prefixMass[i-1] + peptideMass)
    LinearSpectrum = [0]
    for i in range(len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            LinearSpectrum.append(prefixMass[j] - prefixMass[i])
    return map(int, sorted(LinearSpectrum))

def constructAminoAcidMass():
    AminoDict = {}
    with open("integer_mass_table.txt") as aminoAcid:
        codes = aminoAcid.readlines()
        for code in codes:
            code = code.split(" ")
            AminoDict[code[0]] = code[1].strip()
    return AminoDict

def CyclicSpectrum(Peptide, AminoAcidMass):
    prefixMass = [0]*(len(Peptide)+1)
    for i in range(1, len(prefixMass)):
        prefixMass[i] = (prefixMass[i-1] + int(AminoAcidMass[Peptide[i-1]]))
    CyclicSpectrum = [0]
    peptideMass = prefixMass[len(Peptide)]
    for i in range(len(Peptide)):
        for j in range(i+1, len(Peptide)+1):
            CyclicSpectrum.append(prefixMass[j] - prefixMass[i])
            if i > 0 and j < len(Peptide):
                CyclicSpectrum.append(peptideMass - (prefixMass[j] - prefixMass[i]))
    return map(int, sorted(CyclicSpectrum))




if __name__ == "__main__":
    AminoAcidMass = constructAminoAcidMass()
    print(" ".join((CyclicSpectrum("EIDQYVIQKYEKS", AminoAcidMass))))
