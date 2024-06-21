# Sum of Left Leaves

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = []
        def dfs(node:TreeNode, isLeft:bool) -> None:
            if not node: return None
            if isLeft and not node.left and not node.right:
                total.append(node.val)
            dfs(node.left, 1)
            dfs(node.right, 0)
        dfs(root, 0)
        return sum(total)