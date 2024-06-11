# Find the Array Concatenation Value

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r, ans = 0, len(nums)-1, 0

        while l < r:
            ans += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        
        if l == r:
            ans += nums[l]

        return ans