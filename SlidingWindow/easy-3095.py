# Shortest Subarray With OR at Least K I

# Brute force
def bitwise_or(arr: List[int]) -> int:
    res = 0
    for n in arr:
        res |= n
    return res

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        count = 100
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if bitwise_or(nums[i:j+1]) >= k:
                    count = min(count, j-i+1)
        return count if count != 100 else -1
                