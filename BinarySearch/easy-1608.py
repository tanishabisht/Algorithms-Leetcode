# Special Array With X Elements Greater Than or Equal X

# Brute force (O(n))
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)+1):
            if i == len([n for n in nums if n >= i]):
                return i
        return -1

# Using binary search (O(nlogn sorting + nlogn))
def binarySearch(nums:List[int], i:int) -> int:
    l, r = 0, len(nums) - 1
    ans = len(nums)
    while l <= r:
        m = (l+r) // 2
        if nums[m] < i:
            l = m + 1
        else:
            ans = m
            r = m - 1
    return len(nums) - ans

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)+1):
            if i == binarySearch(nums, i):
                return i
        return -1