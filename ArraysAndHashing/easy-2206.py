# Divide Array Into Equal Pairs

# Method 1 - early exit (faster)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for v in counter.values():
            if v & 1 != 0:
                return False
        return True
    

# Method 2 - Slower
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)
        return all(v & 1 == 0 for v in c.values())