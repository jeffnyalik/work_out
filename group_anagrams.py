"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs:List[str])->List[List[str]]:
        def countS(s:str):
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] +=1
            return tuple(counter,)
        
        groups = defaultdict(list)
        for s in strs:
            count = countS(s)
            groups[count].append(s)
        
        return groups.values()
        

cls = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
# strs = [""]
# strs = ["a"]
print(cls.groupAnagrams(strs))