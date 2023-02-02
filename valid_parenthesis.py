"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s:str)->bool:
        if s is None:
            return ""
        
        stack = []
        hashMap = {
            ')':'(','}':'{',']':'['
        }

        for c in s:
            if c not in hashMap:
                stack.append(c)
                continue
            if not stack or stack[-1] != hashMap[c]:
                return False
            stack.pop()
        return not stack


cls = Solution()
s = "()"
# s = "(]"
print(cls.isValid(s))