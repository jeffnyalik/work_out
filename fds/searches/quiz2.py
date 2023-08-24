"""
Given a positive number n and precision p, find the square root of number upto p decimal places using binary search. 
"""

class Solution:
    def squareRoot(self, number, precision):
        low = 0
        high, res = number, 1

        while low <= high:
            middle = low + (high - low) // 2
            if(middle * middle == number):
                res = middle
                break

            if(middle * middle <= number):
                low = middle + 1
                res = middle
            else:
                high = middle - 1

        counter = 0.1
        for i in range(0, precision):
            if(res * res <=number):
                res +=counter
            res = res - counter
            counter = counter / 10
        return res
    

sol = Solution()
print(round(sol.squareRoot(50, 3), 4))
print(round(sol.squareRoot(10, 4), 4))
    
