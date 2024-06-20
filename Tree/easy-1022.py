# Sum of Root To Leaf Binary Numbers

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = []
        def preorder_dfs(node:TreeNode, tmp:str) -> None:
            if not node: return None
            tmp += str(node.val)
            if not node.left and not node.right:
                stack.append(tmp)
                tmp = ''
            preorder_dfs(node.left, tmp)
            preorder_dfs(node.right, tmp)
        preorder_dfs(root, '')
        return sum(int(num,2) for num in stack)