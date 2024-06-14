# Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq._heapify_max(nums)
        n1 = heapq._heappop_max(nums)
        n2 = heapq._heappop_max(nums)
        return (n1-1) * (n2-1)