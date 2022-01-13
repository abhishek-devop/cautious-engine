# Program to Illustrate Bubble Sort
# Author : Abhishek Purbai
def BubbleSort(NumList):
    print("List of Items Before Applying Bubble Sort", NumList)
    i=0
    for n in range(len(NumList)-1,0,-1):
        for i in range (n):
            if NumList[i] > NumList[i+1]:
                NumList[i], NumList[i+1] = NumList[i+1], NumList[i]
    print(NumList)
if (__name__ == "__main__"):
    NumList = [5,1,4,2,8]
    BubbleSort(NumList)
