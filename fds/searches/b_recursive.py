class Solution:
    def binarySearch(self, arr, low, high, key):
        if not arr: return
        if low <= high:
            middle = low + (high - low) //2
            if(arr[middle] == key):
                return middle
            elif(arr[middle] > key):
                return self.binarySearch(arr, low, middle - 1, key)
            return self.binarySearch(arr, middle + 1, high, key)
        return -1

sol = Solution()
arr = [2, 3, 4, 10, 40]
key = 40
     
# Function call
result = sol.binarySearch(arr, 0, len(arr)-1, key)
    
if result != -1:
    print("Element is present at index", result)
else:
    print("Element is not present in array")