# Sum of Unique Elements

# Method 1
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        
        res = 0
        for c in counts:
            if counts[c] == 1:
                res += c
        
        return res
    

# Method 2
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum([c for c in counts if counts[c] == 1])