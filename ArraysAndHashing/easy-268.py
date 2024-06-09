# Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set([n for n in range(len(nums)+1)]) - set(nums)).pop()