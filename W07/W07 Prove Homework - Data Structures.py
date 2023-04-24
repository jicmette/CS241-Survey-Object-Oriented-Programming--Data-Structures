def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)

for n in range(0,20):
    print("Fibonacci({}) = {}".format(n,fib(n)))

