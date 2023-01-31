"""Check if a number is prime number"""

def isPrime(n:int)->bool:
    if not n:
        return 
    
    count = 0
    if n > 1:
        for i in range(1, n+1):
            if n % i == 0:
                count +=1
        if count  == 2:
            return True
        return False

n = 3
print(isPrime(n))