# Kth Missing Positive Number

# O(n + nlogn sorting)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = list(set(range(1, max(arr[-1], len(arr)+k)+1)) - set(arr))
        l.sort()
        return l[k-1]