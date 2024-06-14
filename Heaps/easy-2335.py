# Minimum Amount of Time to Fill Cups

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amt = [-a for a in amount]
        heapq.heapify(amt)
        res = 0
        while True:
            f = heapq.heappop(amt)
            s = heapq.heappop(amt)
            if not f and not s:
                break
            heapq.heappush(amt, f+1) if f else heapq.heappush(amt, f)
            heapq.heappush(amt, s+1) if s else heapq.heappush(amt, s)
            res += 1
        return res