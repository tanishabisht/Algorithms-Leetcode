# Prime Number of Set Bits in Binary Representation

def isPrime(n:int) -> bool:
    if n <= 1:
        return False
    for i in range(2, (n//2) + 1):
        if n%i == 0:
            return False
    return True

def countSetBits(n:int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, right+1):
            setbits = countSetBits(i)
            print(setbits)
            count += 1 if isPrime(setbits) else 0
        return count
        