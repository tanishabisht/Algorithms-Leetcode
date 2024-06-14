# Delete Greatest Value in Each Row

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        res = 0
        for row in grid:
            heapq._heapify_max(row)
        while grid[0]:
            max_elem = 0
            for row in grid:
                max_elem = max(max_elem, heapq._heappop_max(row))
            res += max_elem
        return res