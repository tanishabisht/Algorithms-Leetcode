#  Evaluate Boolean Binary Tree

def dfs(node:TreeNode) -> bool:
    if not node:
        return None
    if not node.left:
        return node.val
    if node.val == 2:
        return dfs(node.left) or dfs(node.right)
    if node.val == 3:
        return dfs(node.left) and dfs(node.right)

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return dfs(root)