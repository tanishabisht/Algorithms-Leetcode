# Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums = [int(math.pow(num,2)) for num in nums]
        nums.sort()
        return nums