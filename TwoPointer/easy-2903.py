# Find Indices With Index and Value Difference I

# Brute Force
def abs(n:int) -> int:
    if n > 0:
        return n
    else:
        return -n

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(j-i) >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    return [i,j]
        return [-1,-1]