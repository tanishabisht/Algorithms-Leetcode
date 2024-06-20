# N-ary Tree Preorder Traversal

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def traversal(node):
            if not node:
                return None
            ans.append(node.val)
            for child in node.children:
                traversal(child)
        traversal(root)
        return ans