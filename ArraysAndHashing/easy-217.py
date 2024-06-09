# Contains Duplicate

# Method 1 - using sets
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    

# Method 2 - Using hashmaps
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for c in counter:
            if counter[c] >= 2:
                return True
        return False