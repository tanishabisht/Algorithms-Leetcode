# Count Pairs Whose Sum is Less than Target

# Brute Force O(n^2)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] < target:
                    count += 1
        return count
    

# Binary search O(nlogn)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums) - 1

            while l <= r:
                m = (l+r) // 2
                if nums[i] + nums[m] < target:
                    count += m - l + 1
                    l = m + 1
                else:
                    r = m - 1
        return count