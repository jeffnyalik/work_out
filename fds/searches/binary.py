class Solution:
    def binarySearch(self, arr, low, high, key):
        if not arr: return
        while low <= high:
            middle = low + (high - low) // 2
            if key == arr[middle]:
                return middle
            elif key > arr[middle]:
                low = middle + 1
            else:
                high = middle - 1
        return -1

sol = Solution()
arr = [2, 3, 4, 10, 40]
res = sol.binarySearch(arr, 0, len(arr)-1, key=2)
if(res != -1): 
    print(f"Element found at {res}")
else:
    print(False)
    
