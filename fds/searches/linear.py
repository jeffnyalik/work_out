class Solution:
    def linearSearch(self, arr, key):
        if not arr: return 
        for i in range(len(arr)):
            if key == arr[i]:
                return True
        return False


sol = Solution()
arr = [2, 3, 4, 10, 40]
res = sol.linearSearch(arr, key=4)
if(res):
    print("The key has been found")
else:
    print("The key does not exist")
