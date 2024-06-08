# N-Repeated Element in Size 2N Array

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return counter.most_common(1)[0][0]