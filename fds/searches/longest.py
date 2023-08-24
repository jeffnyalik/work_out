"""
Input: str = {“geeksforgeeks”, “geeks”, “geek”, “geezer”}

Output: “gee”

Explanation: All the given strings have “gee” prefix common in them, which is the longest them.

Input: {“apple”, “ape”, “april”}

Output: “ap”
"""

class Solution:
    def commonPrefix(self, strs):
        if not strs: return 
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            
            res +=strs[0][i]
        
        return res

sol = Solution()

strs = ["flower", "flow", "flight"]
# strs = ["apple", "ape", "april"]
print(sol.commonPrefix(strs))
                