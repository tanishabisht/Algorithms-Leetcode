# Minimum Distance Between BST Nodes

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node:TreeNode) -> None:
            if not node: return None
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        res.sort()
        ans = 100000
        for i in range(len(res) - 1):
            if res[i+1] - res[i] < ans:
                ans = res[i+1] - res[i]
        return ans