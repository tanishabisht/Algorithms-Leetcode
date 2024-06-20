# Two Sum IV - Input is a BST

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = {}

        def dfs(node:TreeNode):
            if not node: return None
            seen[node.val] = seen.get(node.val, 0) + 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        for key in seen.keys():
            if k - key in seen and k - key != key:
                return True
            if k - key in seen and k - key == key and seen[key] > 1:
                return True

        return False