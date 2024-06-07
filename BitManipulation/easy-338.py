# Counting Bits

def countSetBits(n:int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n+1):
            arr.append(countSetBits(i))
        return arr
        