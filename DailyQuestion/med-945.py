# Minimum Increment to Make Array Unique

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        i = min(0, min(nums))
        for num in nums:
            if i - num > 0:
                count += i - num
            elif i - num < 0:
                i = num
            i += 1
        return count