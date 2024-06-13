# Minimum Difference Between Highest and Lowest of K Scores

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, k-1
        min_dif = nums[r] - nums[l]
        while r < len(nums):
            curr_diff = nums[r] - nums[l]
            min_dif = min(min_dif, curr_diff)
            r += 1
            l += 1
        return min_dif