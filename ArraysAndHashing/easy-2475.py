# Number of Unequal Triplets in Array

# Method 1: O(n^3) complexity - brute force
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1
        return count