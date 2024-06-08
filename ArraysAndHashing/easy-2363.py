# Merge Similar Items

# Method 1
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d1 = Counter({k:v for [k,v] in items1})
        d2 = Counter({k:v for [k,v] in items2})

        res = [[k,v] for k,v in (d1 + d2).items()]
        res.sort()

        return res
    

# Method 2
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d1 = Counter({k:v for [k,v] in items1})
        d2 = Counter({k:v for [k,v] in items2})
        return sorted([[k,v] for k,v in (d1 + d2).items()])