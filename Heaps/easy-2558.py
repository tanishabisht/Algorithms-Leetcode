# Take Gifts From the Richest Pile

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heapq.heappush(heap, -gift)
        while k > 0:
            l = heapq.heappop(heap)
            elem = floor(sqrt(abs(l)))
            heapq.heappush(heap, -elem)
            k -= 1
        return -sum(heap)