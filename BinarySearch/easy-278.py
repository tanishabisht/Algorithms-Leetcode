# First Bad Version

# Using Binary Seach - O(log(len(n)))
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        ans = -1
        while l <= r:
            m = (l+r) >> 1
            if isBadVersion(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans

        