# 

# Method 1 - O(n + nlogn) - using & operation
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for arr in nums[1:]:
            res &= set(arr)
        res_list = list(res)
        res_list.sort()
        return res_list
    
# Method 2 - O(n + nlogn) - using intersection operation
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for arr in nums[1:]:
            res = res.intersection(set(arr))
        res_list = list(res)
        res_list.sort()
        return res_list
    

# Method 3 - Fastest - Since it is mentioned the subarrays are distinct so we found a little formula for that
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        flatnums = list(itertools.chain(*nums))
        counter = Counter(flatnums)
        res = [c for c in counter if counter[c] == n]
        res.sort()
        return res