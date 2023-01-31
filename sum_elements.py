"""Sum all elements in the array"""
from typing import List
def sumElements(arr:List[int])->List[int]:
    res  = 0
    if not arr:
        return []

    for i in range(len(arr)):
        res = res + arr[i]
    
    return res


arr = [1,2,4,6,8,9]
print(sumElements(arr))
