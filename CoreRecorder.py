import timeit #this is used to record the runtime of the functions
from Func_ArrayTimeAverager import avgOfArray #this function is used to calculate the average of the recorded times

def functionTimeRecorder(disregaded_setup, functionList):
    #this function runs the functions (that are being tested),
    #   records how long the functions take to run,
    #   and records that data in as a string to be returned to the main file
    recorder = ""
    for (function,functionInfo) in functionList:
        funct = function
        time = timeit.repeat(setup = disregaded_setup, stmt = funct, number = 1)
        Prompt_Inner = 'For '+str(function)+':'+'\n Info: '+str(functionInfo)+'\n All Execution Speeds: {}'.format(time)+'\n Average Execution Time of this instance After 5 repetitions is {}'.format(avgOfArray(time))+'\n Quickest Execution Time is {}'.format(min(time))+'\n'
        print(Prompt_Inner)
        Prompt_Inner = recorder + '\n' + Prompt_Inner
        recorder = Prompt_Inner
    return recorder