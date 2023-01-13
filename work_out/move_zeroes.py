"""""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""""

"""""
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""""


from typing import List

class Solution:
    def moveZeroes(self, arr:List[int])->int:
        if not arr:
            return arr
        
        l  = 0
        for r in range(len(arr)):
            if arr[r]:
                (arr[l], arr[r]) = (arr[r], arr[l])
                l+=1
        return arr


if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    cls = Solution()
    print(cls.moveZeroes(arr))

## Time Complexity => O(N)
## Space Complexity => O(1)