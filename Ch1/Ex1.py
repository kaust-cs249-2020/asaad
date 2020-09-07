#  1.2 Hidden Messages in the Replication Origin 
def PatternCount(text, pattern):
    #  Input: Strings Text and Pattern.
    #  Output: Count(Text, Pattern).
    count = 0
    step = len(pattern)
    for i in range(len(text)-len(pattern)):
        if(text[i:step+i] == pattern):
            count = count + 1
    return count

if __name__ == "__main__":
    with open('dataset_369233_6.txt', 'r') as file:
        data = file.read().replace("\n", "")
        print(PatternCount(data, "CAGTGGCCA"))
