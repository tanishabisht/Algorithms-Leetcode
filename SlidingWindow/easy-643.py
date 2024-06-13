# Maximum Average Subarray I

# 1st Try
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # initialize
        # left, right = 0, fixed_window_size - 1
        l, r = 0, k-1

        # initialize
        # curr_val = ans_val = perform operation on first k elements
        cur_sum = max_sum = sum(nums[l:r+1])

        # iterate over elements of the array
        while r < (len(nums) - 1):

            # update curr_val
            cur_sum += nums[r+1] - nums[l]

            # update ans_val based on previous value of ans_val and current value of curr_val
            max_sum = max(max_sum, cur_sum)

            # increment left and right
            l += 1
            r += 1

        return max_sum / k