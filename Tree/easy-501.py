# Find Mode in Binary Search Tree

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        seen = {}
        def dfs(node:TreeNode) -> None:
            if not node: return None
            seen[node.val] = seen.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        counter = Counter(seen).most_common()
        return [k for (k,v) in counter if v == counter[0][1]]