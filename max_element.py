"""Maximum element in an array"""
"""Applies also for min element by modifying arr[i] < minElement"""

from typing import List
def findMaxElement(arr:List[int])->List[int]:
    if not arr:
        return []
    
    maxElement = arr[0]
    for i in range(len(arr)):
        if arr[i] > maxElement:
            maxElement = arr[i]
    
    return maxElement


arr = [4,5,6,3,2,9]
print(findMaxElement(arr))