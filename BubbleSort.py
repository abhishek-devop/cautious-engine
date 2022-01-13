# Program to Illustrate Bubble Sort
# Author : Abhishek Purbai
def BubbleSort(NumList):
    print("List of Items Before Applying Bubble Sort", NumList)
    i=0
    j=1
    for i in range (len(NumList)):
        for j in range(len(NumList)):
            if NumList[j] < NumList[i]:
                NumList[i], NumList[j] = NumList[j], NumList[i]
    print(NumList)
if (__name__ == "__main__"):
    NumList = [5,1,4,2,8]
    BubbleSort(NumList)
