# Search in a Binary Search Tree

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return None
        if val > root.val:
            return self.searchBST(root.right, val)
        elif val < root.val:
            return self.searchBST(root.left, val)
        elif val == root.val: 
            return root