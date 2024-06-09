# Find Lucky Integer in an Array

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        for v,f in counter.most_common():
            if v == f:
                return v
        return -1