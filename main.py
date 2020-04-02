import Prompts #file that contains all the prints statements
from File_Manager import fileManager #the function that handles file management
from CoreRecorder import functionTimeRecorder #the core of the application

setup = '''
from test_data import num
from test_data import worstCaseArray
from AlgCycle_1 import AlgorithmCycle
from Func_Fibonacci import Fibonacci
from Func_HeapSort import heapSort
from Func_ReverseElements import ReverseElements
from Func_SortingAlgorithm import SortingAlgProcessor
'''
#when trying to change the test variable -the data that the functions run, change within this string

functionList = [('''ReverseElements(worstCaseArray)''',"This program runs in O(n) time"),
                ('''SortingAlgProcessor(worstCaseArray)''',"This program runs in O(n^2) time"),
                ('''heapSort(worstCaseArray)''',"This program runs in O(n log n) time"),
                ('''Fibonacci(num)''',"This program runs in O(2^n) time"),
                ('''AlgorithmCycle(ReverseElements, SortingAlgProcessor, heapSort, Fibonacci, worstCaseArray, num)''',"This Program runs all 4 previous programs to get a complete time")]

print(Prompts.Prompt_1)
print(Prompts.Prompt_2)

saved_data = functionTimeRecorder(setup, functionList)
#"setup" is a string of all code that i want the processor to ignore when recording the functions runtime
#"functionList" is a list of functions that i want to be timed when it runs. the fire part of the tuple is the function name
#               the second part is info prompts

print(Prompts.Prompt_3)

fileManager(saved_data)
#"saved_data" is a string of data and prompts returned by functionTimeRecorder
#fileManager handles the file dumping work of the application