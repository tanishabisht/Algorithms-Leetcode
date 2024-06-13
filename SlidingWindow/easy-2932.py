# Maximum Strong Pair XOR I

# 1st Try
class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:

        # sort the array
        nums.sort()

        # initialize
        # left, right = 0, 0
        l, r = 0, 0
        
        # initialize
        # max_val = curr_val = 0
        max_xor = curr_xor = 0

        # iterate over elements of the array
        while l < len(nums):

            r = l

            # meet the condition to expand
            while r < len(nums) and (nums[r] - nums[l]) <= nums[l]:
                # process current window
                curr_xor = nums[l] ^ nums[r]
                max_xor = max(max_xor, curr_xor)
                r += 1
            
            # contract the window
            l += 1

        return max_xor