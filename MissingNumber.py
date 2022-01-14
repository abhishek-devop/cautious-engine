# Author : Abhishek Purbai
# Program to find out Missing number in the natural numbers list.
def missing(numlist):
    sumtotal= int(len(numlist)+1)*(int(len(numlist))+2)/2
    print(int(sumtotal))
    result = int(sumtotal) - sum(numlist)
    print("print missing number is", result)
if (__name__ == "__main__"):
    numlist = [1,2,3,4,5,6,7,8,9,10,11,12,14]
    missing(numlist)
