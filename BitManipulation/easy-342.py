# Power of Four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False

        return n & n - 1 == 0 and (n & 0x55555555) != 0