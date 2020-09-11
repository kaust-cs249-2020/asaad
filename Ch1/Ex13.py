#  1.10 Epilogue: Complications in ori Predictions 
from Ex12 import FrequentWordsWithMismatchesAndRC
from Ex6 import minimumSkew
from Ex4 import listToString
if __name__ == "__main__":
    with open('Ch1/covid19_data.txt', 'r') as file:
        data = file.read()
        index = minimumSkew(data)[1][1]
        print("Starting my search from index {} with an offset 1000".format(index))    
        print(listToString(FrequentWordsWithMismatchesAndRC(data[index:], 9, 2)))