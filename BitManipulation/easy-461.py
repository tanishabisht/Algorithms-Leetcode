# Hamming Distance

def countSetBits(n:int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return countSetBits(x ^ y)