# Make Array Zero by Subtracting Equal Amounts

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = [n for n in nums if n != 0]
        heapq.heapify(nums)
        count = 0
        while nums:
            s = heapq.heappop(nums)
            nums = [n-s for n in nums if n-s != 0]
            count += 1
        return count 