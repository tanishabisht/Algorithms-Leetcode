# Find if Path Exists in Graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        graph = {i: [] for i in range(n)}
        for n1, n2 in edges:
            graph[n1] += [n2]
            graph[n2] += [n1]
            
        seen = set([source])

        def dfs(node):
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)