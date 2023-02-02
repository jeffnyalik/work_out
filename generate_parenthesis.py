"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

from typing import List

class Solution:
    def generateParenthesis(s:str, n:int)->List[str]:
        if not n:
            return

        res = []
        stack = []
        def backtracking(open, close):
            if open == close == n:
                res.append("".join(stack))
                return 
            if open < n:
                stack.append("(")
                backtracking(open + 1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtracking(open, close + 1)
                stack.pop()
        backtracking(0, 0)
        return res

cls = Solution()
n = 3
print(cls.generateParenthesis(n))