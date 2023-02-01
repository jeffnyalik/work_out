from typing import List

class Solution:
    def rotate(self, arr:List[int], k:int)->None:
        if not arr:
            return []
        k = k % len(arr)

        l, r = 0, len(arr)-1
        while l < r:
            (arr[l], arr[r]) = (arr[r], arr[l])
            l+=1
            r-=1
        
        l,r = 0, k-1
        while l < r:
            (arr[l], arr[r]) = (arr[r], arr[l])
            l+=1
            r-=1
        
        l,r = k, len(arr)-1
        while l < r:
            (arr[l], arr[r]) = (arr[r], arr[l])
            l+=1
            r-=1
        return arr

cls = Solution()
# arr = [1,2,3,4,5,6,7]
arr = [-1,-100,3,99]
k = 2
print(cls.rotate(arr, k))