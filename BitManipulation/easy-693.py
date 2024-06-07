# Binary Number with Alternating Bits

# Method 1 - Slow
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        n = n >> 1

        while n:
            curr = n & 1
            if prev == curr:
                return False
            prev = curr
            n = n >> 1

        return True
    

# Method 2 - Tiny bit faster
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return n ^ (n >> 1) == (1 << n.bit_length()) - 1


# Method 3 - Fastest
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return x & (x+1) == 0