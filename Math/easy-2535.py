# Difference Between Element Sum and Digit Sum of an Array

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digits = []
        for n in nums:
            ans = [int(i) for i in str(n)]
            print(ans)
            digits += ans
        return sum(nums) - sum(digits)