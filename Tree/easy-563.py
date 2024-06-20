# Binary Tree Tilt

# Bad soln
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        def getSum(node:TreeNode) -> int:
            if not node: return 0
            return node.val + getSum(node.left) + getSum(node.right)

        def tilt(node:TreeNode) -> None:
            global ans
            if not node: return None
            ans += abs(getSum(node.left) - getSum(node.right))
            tilt(node.left)
            tilt(node.right)
        
        global ans
        ans = 0
        tilt(root)
        return ans