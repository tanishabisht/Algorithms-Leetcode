# Count Elements With Maximum Frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = freq.most_common(1)[0][1]
        
        res = 0
        for v in freq.values():
            if v == max_freq:
                res += v

        return res