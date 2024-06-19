# Count Negative Numbers in a Sorted Matrix

# O(n logn) using binary search
def binarySearch(arr: List[int]) -> int:
    l, r = 0, len(arr) - 1
    count = 0
    while l <= r:
        m = (l+r) // 2
        if arr[m] < 0:
            count += r - m + 1
            r = m - 1
        else:
            l = m + 1
    return count


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            count += binarySearch(grid[i])
        return count