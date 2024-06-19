# Arranging Coins

# Brute Force - O(len(n))
class Solution:
    def arrangeCoins(self, n: int) -> int:
        count = 0
        i = 1
        while n > 0:
            n -= i
            i += 1
        return i - 1 if n == 0 else i - 2
    
# Using Binary Search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        ans = -1
        while l <= r:
            m = (l+r) >> 1
            if (m * (m+1) // 2) == n:
                return m
            elif (m * (m+1) // 2) < n:
                ans = m
                l = m + 1
            else:
                r = m - 1
        return ans