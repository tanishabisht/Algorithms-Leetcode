# Apply Operations to an Array

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        nums1 = [n for n in nums if n != 0]
        nums2 = [n for n in nums if n == 0]
        return nums1 + nums2