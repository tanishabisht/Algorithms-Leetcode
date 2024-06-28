# Find Center of Star Graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        seen = {}
        for u,v in edges:
            seen[u] = seen.get(u, 0) + 1
            seen[v] = seen.get(v, 0) + 1
        return [k for k,v in seen.items() if v == n][0]
    

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]