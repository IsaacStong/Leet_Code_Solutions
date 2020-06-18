"""Created by Isaac Stong on 6/17/20
    Solution solves Fibonacci sequence to the
    n-th spot using recursive algorithm"""


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
    else:
        return "Invalid Input"


m = fibonacci(0)
print(m)