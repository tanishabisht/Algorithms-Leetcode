# Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1
            
        seen = {}
        for i in range(len(trust)):
            seen[trust[i][1]] = seen.get(trust[i][1], []) + [trust[i][0]]
        
        vals = []
        for val in seen.values():
            vals += val
        vals = set(vals)

        for k,v in seen.items():
            if len(v) == (n-1) and k not in v and k not in vals:
                return k

        return -1