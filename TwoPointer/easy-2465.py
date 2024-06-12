# Number of Distinct Averages

# Method 1: O(N^2) time complexity
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()
        while len(nums):
            ma, mi = max(nums), min(nums)
            nums.remove(ma)
            nums.remove(mi)
            avg.add((ma+mi)/2)
        return len(avg)
    
# Method 2: O(NLogN) - Sorting
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = set()
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            ma, mi = nums[r], nums[l]
            l += 1
            r -= 1
            avg.add((ma+mi)/2)
        return len(avg)
    
# Method 3: Optimized method 2 - O(NlogN)
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        l, r, avg = 0, len(nums) - 1, set()
        while l < r:
            avg.add((nums[l]+nums[r])/2)
            l += 1
            r -= 1
        return len(avg)