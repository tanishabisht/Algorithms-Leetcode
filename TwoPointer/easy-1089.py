# Duplicate Zeros

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i, n = 0, len(arr)
        while i < n - 1:
            if arr[i] == 0:
                arr[i+2:n] = arr[i+1:n-1]
                arr[i+1] = 0
                i += 1
            i += 1