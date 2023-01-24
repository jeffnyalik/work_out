"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
from typing import List
class Solution:
    def maxArea(self, arr:List[int])->int:
        maxArea = 0
        area = 0

        i = 0
        j = len(arr)-1

        while i < j:
            if(arr[i] > arr[j]):
                area = (j-i) * arr[j]
                j-=1
            else:
                area = (j-i) *arr[i]
                i+=1
            if area > maxArea:
                maxArea = area
        
        return maxArea

        """for i in range(len(arr)):
            for j in range(i, len(arr)):
                area = (j-i) * min(arr[j], arr[i])
                maxArea = max(maxArea, area)
        return maxArea"""

cls = Solution()
arr = [1,8,6,2,5,4,8,3,7]
print(cls.maxArea(arr))
