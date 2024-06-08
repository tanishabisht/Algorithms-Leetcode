# Find the XOR of Numbers Which Appear Twice

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counts = Counter(nums)

        res = 0
        for k in counts:
            if counts[k] == 2:
                res ^= k

        return res