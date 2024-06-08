# Subarrays Distinct Element Sum of Squares I

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        distinctCount = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                distinctCount += math.pow(len(set(nums[i:j+1])), 2)

        return int(distinctCount)