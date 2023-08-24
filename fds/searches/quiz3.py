"""
Given an array arr[] of N distinct integers, the task is to check if this array is sorted when rotated counter-clockwise. A sorted array is not considered sorted and rotated, i.e., there should at least one rotation.

"""
class Solution:
    def find_pivot(self, arr, low, high):
        if not arr: return []
        while low <= high:
            middle = low + (high - low) //2
            if(arr[middle] > arr[middle + 1]):
                return middle
            elif(arr[low] <= arr[middle]):
                low = middle + 1
            else:
                high = middle - 1
        return -1
    
    def is_sorted_rotated(self, arr):
        if not arr: return []
        pivot = self.find_pivot(arr, 0, len(arr)-1)
        if pivot == -1:
            return False
        if pivot == 0:
            return True
        return arr[0] >= arr[len(arr)-1]


sol = Solution()
arr =  [3, 4, 5, 1, 2]
print(sol.is_sorted_rotated(arr))
