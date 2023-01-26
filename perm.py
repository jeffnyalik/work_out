"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

"""

class Solution:
    def checkInclusion(self, s1:str, s2:str)->bool:
        if not s1 and not s2:
            return False
        count = [0] * 26
        for c in s1:
            count[ord(c) - ord('a')] -=1
        for  i, c in enumerate(s2):
            count[ord(c) - ord('a')] +=1
            if i >= len(s1):
                count[ord(s2[i-len(s1)]) - ord('a')] -=1
            if not any(count):
                return True
        
        return False


cls = Solution()
s1 = "ab"
s2 = "eidbaooo"

# s1 = "ab", s2 = "eidboaoo"
print(cls.checkInclusion(s1, s2))