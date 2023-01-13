"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Follow up:

Could you solve this problem in less than O(n) complexity?
"""""
from typing import List

class Solution:
    def findKthPositive(self, arr:List[int], k:int)->int:
        if arr[0] > k:
            return k
        
        left = 0
        right = len(arr)-1

        while(left <= right):
            middle = (left + right) // 2
            if(arr[middle] - (middle + 1) < k):
                left = middle + 1
            else:
                right = middle - 1
        

        return (left + k)


if __name__ == "__main__":
    # arr = [2,3,4,7,11]
    # k = 5

    arr = [1,2,3,4]
    k = 2

    cls = Solution()
    print(cls.findKthPositive(arr, k))

## Time Complexity => O(logN) => Binary Search.
## Space Complexity => O(1)