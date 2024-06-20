# 872. Leaf-Similar Trees

def traverse(node:TreeNode, ans=List[int]) -> None:
    if not node: return None
    traverse(node.left, ans)
    traverse(node.right, ans)
    if not node.left and not node.right:
        ans.append(node.val)
    return ans
        
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        ans1 = traverse(root1, [])
        ans2 = traverse(root2, [])
        return ans1 == ans2