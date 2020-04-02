def Fibonacci(n):
    #input::: a number
    #output::: nth sequence in fibonnaci
    if (n <= 1):
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)