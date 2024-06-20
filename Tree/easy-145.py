# Binary Tree Postorder Traversal

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(node:TreeNode) -> None:
            if not node: return None
            traverse(node.left)
            traverse(node.right)
            ans.append(node.val)
        traverse(root)
        return ans