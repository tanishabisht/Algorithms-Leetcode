# Missing Number

# O(nlogn + logn) - using binary search
def bs(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l+r) // 2
        if (nums[m] != m):
            r = m - 1
        else:
            l = m + 1
    return l

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        return bs(nums)