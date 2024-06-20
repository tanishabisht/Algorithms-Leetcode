# Increasing Order Search Tree

def inorder(node:TreeNode, stack:List[TreeNode]) -> None:
    if node:
        inorder(node.left, stack)
        stack.append(node.val)
        inorder(node.right, stack)

def buildTree(stack:List[TreeNode]) -> TreeNode:
    if stack:
        return TreeNode(stack[0], right=buildTree(stack[1:]))

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = []
        inorder(root, stack)
        return buildTree(stack)