# Maximum Count of Positive Integer and Negative Integer


# O(n) - using array manipulation
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = len([n for n in nums if n > 0])
        neg = len([n for n in nums if n < 0])
        return max(pos, neg)
        
# O(logn) - using binary search
def binarySearchPos(nums:List[int]) -> int:
    l, r = 0, len(nums) - 1
    ans = -1
    while l <= r:
        m = (l+r) // 2
        if nums[m] > 0:
            ans = m
            r = m - 1
        else:
            l = m + 1
    if ans == -1:
        return 0
    return len(nums) - ans


def binarySearchNeg(nums:List[int]) -> int:
    l, r = 0, len(nums) - 1
    ans = -1
    while l <= r:
        m = (l+r) // 2
        if nums[m] < 0:
            ans = m
            l = m + 1
        else:
            r = m - 1
    if ans == -1:
        return 0
    return ans + 1

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = binarySearchPos(nums)
        neg = binarySearchNeg(nums)
        return max(pos, neg)
    



# GOOD SOLN
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        first_pos = self.find_first_positive(nums)
        last_neg = self.find_last_negative(nums)
        return max(last_neg + 1, len(nums) - first_pos)

    def find_first_positive(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (right+left) // 2
            if nums[mid] > 0:
                right = mid
            else:
                left = mid + 1
        return left
    
    def find_last_negative(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (right+left) // 2
            if nums[mid] >= 0:
                right = mid
            else:
                left = mid + 1
        return left - 1