# Last Stone Weight

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            h1 = heapq.heappop(heap)
            h2 = heapq.heappop(heap)
            if h1 != h2:
                heapq.heappush(heap, h1 - h2)
        return 0 if not heap else -heapq.heappop(heap)
