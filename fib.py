"""Fibonacci number"""
def fib(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        res = fib(n-1) + fib(n-2)
    return res


n = 9
print(fib(n))