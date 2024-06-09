# Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return set(range(1,len(nums)+1)) - set(nums)