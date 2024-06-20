# N-ary Tree Postorder Traversal

def traversal(root:'Node', ans:List[int]) -> None:
    if root:
        for child in root.children:
            traversal(child, ans)
        ans.append(root.val)
    
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        traversal(root, ans)
        return ans