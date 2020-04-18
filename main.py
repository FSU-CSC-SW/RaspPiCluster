import Prompts #file that contains all the prints statements
from File_Manager import fileManager, Para_fileManager, fileManager_Autosaver, Para_fileManager_Autosaver #the function that handles file management
from CoreRecorder import functionTimeRecorder #the core of the application
from multiprocessing import freeze_support
from Para_Feature_Recorder import sequentialFunctions, sequentialFunctionsExtentensiveEdition, parallelizedFunctions, parallelizedFunctionsExtensiveEdition
import atexit

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


if __name__ == '__main__':

    parallelProcessing = str(input("Enter 0 for sequential and 1 for Parallel Processing: "))
    while parallelProcessing != "0" and parallelProcessing != "1":
    #input validation
        parallelProcessing = str(input("Enter 0 for sequential and 1 for Parallel Processing: "))

    if parallelProcessing == "1":
        freeze_support()
        test_data_selection = str(input("Enter 0 for Light Test Case and 1 for Heavy Test Case: "))

        while test_data_selection != "0" and test_data_selection != "1" and test_data_selection != "3":
        #input validation
            parallelProcessing = str(input("Enter 0 for sequential and 1 for Parallel Processing: "))

        if test_data_selection == "0":
        #parallel algorithms under light load
            print(Prompts.Prompt_1)
            print(Prompts.Prompt_2)
            recorded_times = [sequentialFunctions(), parallelizedFunctions()]
            saved_data = Prompts.Printer(recorded_times)
            print(Prompts.Prompt_3)
            atexit.register(Para_fileManager_Autosaver, saved_data, "light")

        elif test_data_selection == "3":
        #parallel algorithms under both heavy and light load
            print(Prompts.Prompt_dev)
            print(Prompts.Prompt_2)
            recorded_times = [sequentialFunctions(), parallelizedFunctions(), sequentialFunctionsExtentensiveEdition(), parallelizedFunctionsExtensiveEdition()]
            saved_data = Prompts.Printer(recorded_times)
            print(Prompts.Prompt_3)
            atexit.register(Para_fileManager_Autosaver, saved_data, "dev")

        else:
        #parallel algorithms under heavy load
            print(Prompts.Prompt_1_Extensive)
            print(Prompts.Prompt_2)
            recorded_times = [sequentialFunctionsExtentensiveEdition(), parallelizedFunctionsExtensiveEdition()]
            saved_data = Prompts.Printer(recorded_times)
            print(Prompts.Prompt_3)
            atexit.register(Para_fileManager_Autosaver, saved_data, "extensive")


    else:
    #sequntial algorithms
        print(Prompts.Prompt_1)
        print(Prompts.Prompt_2)
        saved_data = functionTimeRecorder(setup, functionList)
        print(Prompts.Prompt_3)
        atexit.register(fileManager_Autosaver, saved_data)