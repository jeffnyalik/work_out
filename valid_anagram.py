"""

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter
class Solution:
    def isAnagram(self, s:str, t:str)->bool:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] +=1
        for c in t:
            counter[ord(c) - ord('a')] -=1
        return not any(counter)

        """return Counter(s) == Counter(t)"""


cls = Solution()
s = "anagram"
t = "nagaram"
print(cls.isAnagram(s, t))