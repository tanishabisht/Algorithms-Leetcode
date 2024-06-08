# Count Number of Pairs With Absolute Difference K

# Method 1: Brute Force
def absoluteDifference(n:int) -> int:
    if n >= 0:
        return n
    else:
        return -n

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if absoluteDifference(nums[i] - nums[j]) == k:
                    counter += 1

        return counter
    
# Method 2
