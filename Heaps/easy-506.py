# Relative Ranks

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        res = [""] * len(score)
        heap = []
        for i,v in enumerate(score):
            heapq.heappush(heap, (-v, i))
        mapping = {0:'Gold Medal', 1:'Silver Medal', 2:'Bronze Medal'}
        for rank in range(len(res)):
            large, i = heapq.heappop(heap)
            res[i] = mapping.get(rank, str(rank + 1))
        return res