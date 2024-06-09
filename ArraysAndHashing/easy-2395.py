# Find Subarrays With Equal Sum

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res = []
        for i in range(len(nums) - 1):
            res.append(sum(nums[i:i+2]))
        counter = Counter(res)
        for c in counter:
            if counter[c] >= 2:
                return True
        return False