# Keep Multiplying Found Values by Two

# Method 1 - O(n) time complexity
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original