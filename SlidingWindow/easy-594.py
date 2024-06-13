# Longest Harmonious Subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        l, r = 0, 0
        count = 0
        nums.sort()
        while r < len(nums):
            while (nums[r] - nums[l]) > 1:
                l += 1
            if nums[r] - nums[l] == 1:
                count = max(count, r-l+1)
            r += 1
        return count