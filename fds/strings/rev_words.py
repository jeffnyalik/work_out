"""
Reverse words in a string using stack.
1. split the input string into words
2. add the words in a stack.
3. remove/pop the words and conactenate them in reverse order
"""

class Solution:
    def reverse_words(self, input_string):
        if not input_string:
            return ""
        words = input_string.split()
        stack = []
        for word in words:
            stack.append(word)
        
        rev =  ""
        while stack:
            rev += stack.pop() + " "
        return rev.strip()

sol = Solution()
input_string = " Computer programming  "
print(sol.reverse_words(input_string))
    