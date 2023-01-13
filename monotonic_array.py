"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""

from typing import List

class Solution:
    def monotonicArray(self, arr:List[int])->int:
        if len(arr) == 1:
            return True

        dec = True
        inc = True

        for i in range(1, len(arr)):
            if(arr[i] > arr[i-1]):
                dec = False
            if(arr[i] < arr[i-1]):
                inc = False
        
        return (dec or inc)

if __name__ == "__main__":
    arr = [6, 5, 4, 4] ## True
    # arr = [1,3,2] ## False
    cls = Solution()
    print(cls.monotonicArray(arr))
