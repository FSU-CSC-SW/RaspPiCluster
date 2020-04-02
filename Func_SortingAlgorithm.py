#this file contains all the functions for the sorting algorithm. Currently, not all the functions are being used

def PreSortingAlgorithm(i):
    #input::: number
    #output::: array of numbers in ascending order
    #time-complexity::: O(n^2) + SortingAlgWorstCasePrepper
    #Purporse::: is used when the time complexity of
    #   SortingAlgWorstCasePrepper is negligible.
    #   An integer goes in and the prepper makes a list in descending order
    #       of the numbers from one to n. Then passes it to the sorting algorithm
    arr = SortingAlgWorstCasePrepper(i)
    SortingAlgProcessor(arr)
    return arr

def SortingAlgorithm(a):
    #input::: array of numbers
    #output::: array of numbers in ascending order
    #time-complexity::: worst case-O(n^2), average case-O(n log n)
    #Purporse::: is used when you want to be the one to pass a created
    #   array of numbers to the sorting algorithm
    SortingAlgProcessor(a)
    return a

def SortingAlgWorstCasePrepper(i):
    #input::: number
    #output::: array of numbers in descending order from n to 1
    #time-complexity::: to be determined
    #Purpose::: algorithm was created to generate the worst case for the sorting algorithm processor
    x = [x for x in range(i+1)]
    x = x[:0:-1] #runs in O(n) time
    return(x)


def SortingAlgProcessor(a):
    #input::: number
    #output::: array of numbers in descending order
    #time-complexity::: this algorithmn's worst case is O(n^2)
    sortedBoolean = True
    for index in range(len(a)-1):
        if a[index] > a[index+1]:
            a[index], a[index+1] = a[index+1], a[index]
            sortedBoolean = False
    if sortedBoolean == False:
        SortingAlgProcessor(a)
    else:
        return(a)