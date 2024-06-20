# 

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def dfs(node:TreeNode) -> None:
            if not node: return None
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
        dfs(root)
        return all([n==ans[0] for n in ans])