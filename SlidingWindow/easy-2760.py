# Longest Even Odd Subarray With Threshold

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l, r = 0, 0
        size = 0
        while r < len(nums):
            if nums[l]%2 != 0 or nums[l] > threshold or nums[r] > threshold or (r and nums[r]%2==nums[r-1]%2):
                l = r
            if nums[l]%2 == 0 and nums[l]<=threshold:
                size = max(size, r-l+1)
            r += 1
        return size