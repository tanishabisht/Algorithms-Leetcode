# How Many Numbers Are Smaller Than the Current Number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sorted(nums).index(n) for n in nums]