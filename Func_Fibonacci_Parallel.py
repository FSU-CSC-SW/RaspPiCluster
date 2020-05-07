import platform 
from mpi4py import MPI

# def Fibonacci(n):
#    #input::: a number
#    #output::: nth sequence in fibonnaci
#    if (n <= 1):
#        return 1
#    else:
#        return Fibonacci(n - 1) + Fibonacci(n - 2)


rank = MPI.COMM_WORLD.Get_rank()
size = MPI.COMM_WORLD.Get_size()
FibArray = [0,1] 
  
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
  
# Driver Program 
  
print(fibonacci(9)) 
