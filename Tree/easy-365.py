# Average of Levels in Binary Tree

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        def bfs(node:TreeNode) -> None:
            queue = deque([node])
            while queue:
                n = len(queue)
                row = 0
                for _ in range(n):
                    node = queue.popleft()
                    if not node: return None
                    row += node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                ans.append(row / n)
        bfs(root)
        return ans