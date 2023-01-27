"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

from typing import List
from collections import deque
from collections import deque
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        res = []
        qi = deque()
        
        for i in range(k):
            while qi and arr[i] >= arr[qi[-1]]:
                qi.pop()
            qi.append(i)

        
        for i in range(k, len(arr)):
            res.append(arr[qi[0]])
            while qi and arr[qi[0]] <= i-k:
                qi.popleft()
            while qi and arr[i] >= arr[qi[-1]]:
                qi.pop()
            qi.append(i)
        
        res.append(arr[qi[0]])
        return res





cls = Solution()   
arr = [1,3,-1,-3,5,3,6,7],
k = 3 
print(cls.maxSlidingWindow(arr, k))