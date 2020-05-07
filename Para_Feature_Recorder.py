from mpi4py import MPI
import concurrent.futures
#from multiprocessing import Prcoess, freeze_support
from concurrent.futures import wait
from multiprocessing import Value, Array
from Func_ArrayTimeAverager import avgOfArray #this function is used to calculate the average of the recorded times
import time
from test_data import num, worstCaseArray, num_Extensive, worstCaseArray_Extensive
from AlgCycle_1 import AlgorithmCycle
from Func_Fibonacci import Fibonacci
from Func_HeapSort import heapSort
from Func_ReverseElements import ReverseElements
from Func_SortingAlgorithm import SortingAlgProcessor
import atexit

def parallelizedFunctions():
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = []
        f1 = executor.submit(ReverseElements, worstCaseArray)
        futures.append(f1)
        f2 = executor.submit(SortingAlgProcessor, worstCaseArray)
        futures.append(f2)
        f3 = executor.submit(heapSort, worstCaseArray)
        futures.append(f3)
        f4 = executor.submit(Fibonacci, num)
        futures.append(f4)
        wait(futures)
        finish = time.perf_counter()
        return(f'The Algorthimms, when ran synchronously, finished in {round(finish-start, 2)} second(s)')

def parallelizedFunctionsExtensiveEdition():
    start = time.perf_counter()
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    if rank == 0:
        listReturn = []
        data0 = ReverseElements(worstCaseArray_Extensive) 
        listReturn.append(data0)
    if rank == 1:
        data1 = SortingAlgProcessor(worstCaseArray_Extensive)
        comm.send(data1, dest=0, tag=10)
    if rank == 2:
        data2 = heapSort(worstCaseArray_Extensive)
        comm.send(data2, dest=0, tag=10)
    if rank == 3:
        data3 = Fibonacci(num_Extensive)
        comm.send(data3, dest=0, tag=10)
    if rank == 0:
        data1 = comm.recv(source = 1)
        #complete1 = data1.wait()
        data2 = comm.recv(source = 2)
        #complete2 = data2.wait()
        data3 = comm.recv(source = 3)
        #complete3 = data3.wait()
        print(data3)
    finish = time.perf_counter()
    return(f'The Algorthimms under heavy load, when ran synchronously, finished in {round(finish-start, 2)} second(s)')

def sequentialFunctions():
    start = time.perf_counter()
    results = []
    f1 = ReverseElements(worstCaseArray)
    results.append(f1)
    f2 = SortingAlgProcessor(worstCaseArray)
    results.append(f2)
    f3 = heapSort(worstCaseArray)
    results.append(f3)
    f4 = Fibonacci(num)
    results.append(f4)
    finish = time.perf_counter()
    return(f'The Algorthimms, when ran sequentially, finished in {round(finish-start, 2)} second(s)')

def sequentialFunctionsExtentensiveEdition():
#    comm = MPI.COMM_WORLD
#    rank = comm.Get_rank()
    start = time.perf_counter()
#    if rank == 0:
    ReverseElements(worstCaseArray_Extensive)
    SortingAlgProcessor(worstCaseArray_Extensive)
    heapSort(worstCaseArray_Extensive)
    Fibonacci(num_Extensive)
    finish = time.perf_counter()
    return(f'The Algorthimms under heavy load, when ran sequentially, finished in {round(finish-start, 2)} second(s)')

#print ("This module's name is: {}".format(__name__))
#print("yeet")

if __name__ == '__main__':
    #freeze_support()
    recorded_times = [sequentialFunctions(), parallelizedFunctions(), sequentialFunctionsExtentensiveEdition(), parallelizedFunctionsExtensiveEdition()]
    #print(recorded_times)
    #break

#if __name__ == "Para_Feature_Recorder":
#    recorded_times = [sequentialFunctions(), parallelizedFunctions(), sequentialFunctionsExtentensiveEdition(), parallelizedFunctionsExtensiveEdition()]
#    p1 = Prcoess(Target = f1)
    #print(recorded_times)

#AlgorithmRecorderForParallelismAndSequentialComparison()

def f1():
    start = time.perf_counter()
    ReverseElements(worstCaseArray)
    SortingAlgProcessor(worstCaseArray)
    heapSort(worstCaseArray)
    Fibonacci(num)
    finish = time.perf_counter()
    return(f'The Algorthimms, when ran sequentially, finished in {round(finish-start, 2)} second(s)')
