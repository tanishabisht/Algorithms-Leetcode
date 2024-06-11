# Largest Positive Integer That Exists With Its Negative

def abs(n:int) -> int:
    if n > 0:
        return n
    else:
        return -n

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        m = -1001
        for n in nums:
            if n in seen:
                m = max(m, abs(n))
            else:
                seen.add(-n)
        return -1 if m == -1001 else m