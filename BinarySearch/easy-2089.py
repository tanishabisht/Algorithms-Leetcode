# Find Target Indices After Sorting Array


# Using binary search: O(nlogn) Sorting + O(logn)
def binarySearchHigh(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == target:
            ans = m
            l = m + 1
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return ans

def binarySearchLow(arr: List[int], target: int) -> int:
    l, r = 0, len(arr) - 1
    ans = -1
    while l <= r:
        m = (l+r) // 2
        if arr[m] == target:
            ans = m
            r = m - 1
        elif arr[m] > target:
            r = m - 1
        else:
            l = m + 1
    return ans

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        low, high = binarySearchLow(nums,target), binarySearchHigh(nums,target)
        if low != -1 and high != -1:
            return range(low,high+1)
        elif low == -1 and high != -1:
            return [high]
        elif low != -1 and high == -1:
            return [low]
        else:
            return []
        

# Smaller code: O(nlogn) sorting + O(n)
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        return [i for i in range(len(nums)) if nums[i] == target]