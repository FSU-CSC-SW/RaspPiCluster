#this function is included in the setup of the main function.

def AlgorithmCycle(func1, func2, func3, func4, arr, num):
    #this function is an algorithms with predetermined function names passed to it
    func1(arr) #runs O(n) algorithm
    func2(arr) #runs O(n^2) algorithm
    func3(arr) #runs O(n log n algorithm)
    func4(num) #runs in O(2^n)