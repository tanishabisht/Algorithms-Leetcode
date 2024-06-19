# The K Weakest Rows in a Matrix

# Method 1: O(n) + O(nlogn) sorting + O(k) ==> O(n + nlogn)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts = []
        for i in range(len(mat)):
            counts.append((mat[i].count(1),i))
        counts.sort()
        return [i for (v,i) in counts[:k]]