# Find a Corresponding Node of a Binary Tree in a Clone of That Tree

# Using iteration
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]

        while stack:
            node_original, node_cloned = stack.pop()

            if node_original == target:
                return node_cloned

            if node_original.left:
                stack.append((node_original.left, node_cloned.left))

            if node_original.right:
                stack.append((node_original.right, node_cloned.right))

        return None
    
# Using recursion
def dfs(node:TreeNode, clone:TreeNode, target: TreeNode) -> TreeNode:
    if not node:
        return None
    if node == target:
        return clone
    return dfs(node.left, clone.left, target) or dfs(node.right, clone.right, target)

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return dfs(original, cloned, target)