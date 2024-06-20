# Range Sum of BST

# Using iteration
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        ans = 0

        while stack:
            node = stack.pop()

            if node.val >= low and node.val <= high:
                ans += node.val
            
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return ans
    
# Using recursion
def dfs(node:TreeNode, high:int, low:int) -> int:
    if not node:
        return 0
    ans = 0
    if node.val >= low and node.val <= high:
        ans += node.val
    return dfs(node.left, high, low) + dfs(node.right, high, low) + ans
    
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return dfs(root, high, low)