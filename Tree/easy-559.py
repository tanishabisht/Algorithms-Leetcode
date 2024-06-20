# Maximum Depth of N-ary Tree

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def traverse(node:'Node', depth) -> int:
            if not node: return depth
            return max([traverse(child, depth) for child in node.children], default=0) + 1
        return traverse(root, 0)