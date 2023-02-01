"""Multiply all numbers in the list"""

def multiply(arr):
    res = 1
    for i in range(len(arr)):
        res*=arr[i]

    return res


arr = [3,2,4]
print(multiply(arr))