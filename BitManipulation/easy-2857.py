# Sum of Values at Indices With K Set Bits

def count_set_bits(n:int):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            if count_set_bits(i) == k:
                total += nums[i]
        return total