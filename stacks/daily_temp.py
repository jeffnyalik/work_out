from typing import List
class Solution:
    def dailyTemperatures(self, temperatures:List[int])->List[int]:
        stack = []
        n = len(temperatures)
        answer = [0] * n
        

        for i in range(n):
            while len(stack) != 0 and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]]  = i - stack[-1]
                stack.pop(-1)
            stack.append(i)
        
        return answer
    
cls = Solution()
# temperatures = [73,74,75,71,69,72,76,73]
# temperatures = [30,40,50,60]
temperatures = [30,60,90]
print(cls.dailyTemperatures(temperatures))