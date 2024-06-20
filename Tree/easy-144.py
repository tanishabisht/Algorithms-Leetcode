# Binary Tree Preorder Traversal

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def traverse(node:TreeNode) -> None:
            if not node: return None
            ans.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ans