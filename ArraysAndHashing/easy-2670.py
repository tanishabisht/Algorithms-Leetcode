# Find the Distinct Difference Array

# Method 1 - 110ms
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return res
    
# Method 2 - 94ms
class Solution:
    @staticmethod
    def distinctDifferenceArray(nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return res