"""
Given an array, find the most frequent element in it. If there are multiple elements that appear a maximum number of times, print any one of them.

Examples: 

Input : arr[] = {1, 3, 2, 1, 4, 1}
Output : 1
Explanation: 1 appears three times in array which is maximum frequency.

Input : arr[] = {10, 20, 10, 20, 30, 20, 20}
Output : 20
"""
from typing import List
from collections import defaultdict
class Solution:
    ##Time and Space Complexity  => O(N) and O(N)
    def mostFrequent(self, arr:List[int])->int:
        hashMap = defaultdict(lambda:0)
        for i in range(len(arr)):
            if(arr[i] in hashMap):
                hashMap[arr[i]]+=1
            else:
                hashMap[arr[i]] = 1
        
        ## max frequency count
        max_count = 0
        res  = -1
        for i in hashMap:
            if(max_count < hashMap[i]):
                res = i
                max_count = hashMap[i]
        return res
    """ maxCount = 0
    maxFreqCount = 0
    for i in range(len(arr)):
        count = 0
        for j in range(i+1, len(arr)):
            if(arr[i] == arr[j]):
                count +=1
        if(count > maxCount):
            maxCount = count
            maxFreqCount = arr[i]
    return maxFreqCount

    Time and Space Complexity  => O(N^2) and O(1)
    
    """

if __name__ == "__main__":
    arr = [40,50,30,40,50,30,30]
    cls = Solution()
    print(cls.mostFrequent(arr))