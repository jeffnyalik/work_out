"""Factorial of a number"""

def factorial(n:int)->int:
    """
    Sol 1
    """
    # res = 1
    # for i in range(1, n+1):
    #     if(n == 0 or n ==1):
    #         return 1
    #     res = res * i
    
    # return res

    """
    Sol 2
    """
    if(n == 0 or n == 1):
        return 1
    return n*factorial(n-1)


n = 5
print(factorial(n))