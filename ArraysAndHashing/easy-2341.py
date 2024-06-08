# Maximum Number of Pairs in Array

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        pairs = sum([v//2 for v in counter.values()])
        leftovers = sum([v%2 for v in counter.values()])

        return [pairs, leftovers]