#  1.3 Some Hidden Messages are More Surprising than Others 
def reverseComplement(pattern):
    # Input: A DNA string Pattern.
    # Output: Patternrc , the reverse complement of Pattern.
    DNAmap = {"A":"T", "T":"A", "G":"C", "C":"G",}  # For mapping translation
    
    rcPattern = ""
    for i in range(len(pattern)-1, -1, -1): # Start from the end of the string, range(START, END, INCREMENT).
        # The loop terminates immediately when i == -1
        rcPattern = rcPattern + (DNAmap.get(pattern[i]))
    return rcPattern



if __name__ == "__main__":
    with open('dataset_369233_6.txt', 'r') as file:
        data = file.read().replace("\n", "")
        print(reverseComplement(data))
