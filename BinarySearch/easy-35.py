# Search Insert Position

# Using binary search - left insertion
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) >> 1
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l