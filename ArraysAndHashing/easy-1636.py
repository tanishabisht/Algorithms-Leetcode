# Sort Array by Increasing Frequency

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        print(counter)
        return sorted(nums, key=lambda n: (counter[n], -n))