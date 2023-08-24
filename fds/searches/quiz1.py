"""
Given a sorted array of Strings arr and a String x, find an index of x if it is present in the array, using Binary Search

Examples:

Input: arr[] = {“contribute”, “geeks”, “ide”, “practice”}, x = “ide”
Output:  2
Explanation: The String x is present at index 2.

Input :  arr[] = {“contribute”, “geeks”, “ide”, “practice”}, x = “zz”
Output :  -1
Explanation: The String “zz” is not present. 

"""

class Solution:
    def linearSearch(self, arr, x):
        if not arr: return
        for i in range(len(arr)-1):
            if arr[i] == x: return i
        return -1
    
    def binarySearch(self, arr, low, high, x):
        if not arr: return
        while low <= high:
            middle = low + (high - low) // 2
            if(x == arr[middle]):
                return middle
            elif(x > arr[middle]):
                low = middle + 1
            else:
                high = middle - 1
        
        return -1
    
    def recursiveBin(self, arr, low, high, x):
        if high > low:
            middle = low + (high - low) // 2
            if(x == arr[middle]):
                return middle

            elif(x < arr[middle]):
                return self.binarySearch(arr, low, middle - 1, x)
            else:
                return self.binarySearch(arr, middle + 1, high, x)
        
        return -1
    

sol = Solution()
arr = ["contribute", "geeks", "ide", "practice"]
# res = sol.linearSearch(arr, x="idesdf")
# res = sol.binarySearch(arr, 0, len(arr)-1, x="ide")
res = sol.recursiveBin(arr, 0, len(arr)-1, x="practice")


if res == -1:
    print("The string value does not exist")
else:
    print(f"The string value index is: {res}")

# arr2 = ["contribute", "geeks", "ide", "practice"]