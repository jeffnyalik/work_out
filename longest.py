"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List
class Solution:
    def longestConsecutive(self, arr:List[int])->int:
        res = 0
        hashSet = set()

        for el in arr:
            hashSet.add(el)
        
        for i in range(len(arr)):
            if(arr[i]-1 not in hashSet):
                j = arr[i]
                while(j in hashSet):
                    j+=1
                res = max(res, j-arr[i])
        
        return res
        
        """arr.sort()
        res = 0
        count = 0
        vector = []
        vector.append(arr[0])

        for i in range(1, len(arr)):
            if(arr[i] != arr[i-1]):
                vector.append(arr[i])

        for i in range(len(vector)):
            if(i > 0 and vector[i] == vector[i-1] + 1):
                count +=1
            else:
                count = 1
            res = max(res, count)
        
        return res"""

cls = Solution()
arr = [100,4,200,1,3,2]
# arr = [0,3,7,2,5,8,4,6,0,1]
print(cls.longestConsecutive(arr))