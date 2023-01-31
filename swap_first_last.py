"""Swap first with the last element"""
"""Two approaches"""

from typing import List
def swapFirstLast(arr:List[int])->List[int]:
    if not arr:
        return []

    ## Option one by temp variable
    # temp = arr[0]
    # size = len(arr)
    # arr[0] = arr[size - 1]
    # arr[size - 1] = temp

    ## Option Two
    arr[0],arr[-1] = arr[-1],arr[0]

    return arr

arr = [12, 35, 9, 56, 24]
print(swapFirstLast(arr))