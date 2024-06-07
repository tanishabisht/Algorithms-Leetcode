# Binary Prefix Divisible By 5

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = [True] * len(nums)

        s = 0

        for i, num in enumerate(nums):
            s = (s << 1) + num
            res[i] = s % 5 == 0

        return res