# Merge Two Binary Trees

def dfs(root1:TreeNode, root2:TreeNode) -> TreeNode:
    if not root1:
        return root2

    elif not root2:
        return root1
    
    else:
        res = TreeNode(root1.val + root2.val)
        res.left = dfs(root1.left, root2.left)
        res.right = dfs(root1.right, root2.right)
        return res

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return dfs(root1, root2)