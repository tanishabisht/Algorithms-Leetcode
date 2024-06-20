# Binary Tree Inorder Traversal

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traversal(node:TreeNode) -> None:
            if node:
                traversal(node.left)
                ans.append(node.val)
                traversal(node.right)
        traversal(root)
        return ans