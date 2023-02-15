"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""
from typing import List
class Solution:
    def wordBreak(self, word:str, words:List[str])->bool:
        ## Solution 1
        # if not word: return True
        # for i in range(1, len(word)+ 1):
        #     prefix = word[:i]
        #     if(prefix in words and self.wordBreak(word[i:], words)):
        #         return True
        # return False

        ##Solution 2
        dp = [False for i in range(len(word) + 1)]
        dp[0] = True
        for i in range(len(word) + 1):
            for j in range(i):
                if(dp[j] and word[j:i] in words):
                    dp[i] = True
                    break
        
        return dp[len(word)]


cls = Solution()
# word = "catsandog"
# words = ["cats","dog","sand","and","cat"]

word = "applepenapple"
words = ["apple","pen"]
print(cls.wordBreak(word, words))