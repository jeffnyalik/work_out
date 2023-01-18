"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
 

Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""

from typing import List
from heapq import heappop, heapify, heappush
class Solution:
    def findKthLargest(self, arr:List[int])->int:
        heap = []
        heapify(heap)
        for ar in arr:
            heappush(heap, ar)
            if(len(heap) > k):
                heappop(heap)
        
        return heappop(heap)
        """arr.sort()
        return arr[len(arr)-k]
        Time and Space => O(NlogN) and O(N) or O(1) depends on Mergesort or Quicksort
        """



arr = [3,2,1,5,6,4]
k = 1
cls = Solution()
print(cls.findKthLargest(arr))