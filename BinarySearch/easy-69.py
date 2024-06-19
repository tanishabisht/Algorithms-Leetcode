# Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x//2
        ans = 0
        
        if x == 0 or x == 1:
            return x
        
        while l <= r:
            m = (l + r) // 2
            if m*m == x:
                return m
            elif m*m < x:
                l = m + 1
                ans = m
            else:
                r = m - 1
        return ans