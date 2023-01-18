
"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from heapq import heappush, heappushpop
from typing import List
class Solution:
    def topKFrequent(self, nums:List[int], k:int)->int:
        heap = []
        freq = dict()

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num]+=1
        
        for val, key in freq.items():
            if(len(heap) < k):
                heappush(heap, [val, key])
            else:
                heappushpop(heap, [val, key])
        
        return [key for val, key in heap]

if __name__ == "__main__":
    # nums  = [6, 1, 1, 1, 2, 2, 3]
    nums =  [1,1,1,2,2,3]
    k = 2
    cls = Solution()
    print(cls.topKFrequent(nums, k))