# Find Subsequence of Length K With the Largest Sum

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = nums[:]
        heapq.heapify(heap)
        hashmap = Counter(heapq.nlargest(k, heap))
        res = []
        for n in nums:
            if n in hashmap:
                res.append(n)
                if hashmap[n] == 1:
                    del hashmap[n]
                else:
                    hashmap[n] -= 1
        return res