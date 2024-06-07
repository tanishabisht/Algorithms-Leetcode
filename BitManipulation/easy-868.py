# Binary Gap

class Solution:
    def binaryGap(self, n: int) -> int:
        gap_arr = []
        i = 0

        while n:
            if n & 1:
                gap_arr.append(i)
            i += 1
            n = n >> 1

        max_gap = 0
        for i in range(len(gap_arr) - 1):
            max_gap = max(max_gap, gap_arr[i+1] - gap_arr[i])

        return max_gap
        