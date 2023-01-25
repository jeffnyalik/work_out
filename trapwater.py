"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List

class Solution:
    def trap(self, arr:List[int])->int:
        l = 0
        r  = len(arr)-1

        lmax = 0
        rmax = 0
        trapped_water = 0

        while l <= r:
            if(arr[l] < arr[r]):
                if(arr[l] > lmax):
                    lmax = arr[l]
                else:
                    trapped_water = trapped_water + lmax - arr[l]
                l +=1
            else:
                if(arr[r] > rmax):
                    rmax = arr[r]
                else:
                    trapped_water = trapped_water + rmax - arr[r]
                r -=1
        return trapped_water
        

        """if len(arr) <= 2:
            return 0
        trapped_water = 0
        for i in range(len(arr)):
            leftMax = 0
            for j in range(i, -1, -1):
                leftMax = max(leftMax, arr[j])
            rightMax = 0
            for j in range(i, len(arr)):
                rightMax = max(rightMax, arr[j])
            trapped_water = trapped_water + min(leftMax, rightMax) - arr[i]
        
        return trapped_water"""
        

cls = Solution()
arr = [4,2,0,3,2,5]
print(cls.trap(arr))