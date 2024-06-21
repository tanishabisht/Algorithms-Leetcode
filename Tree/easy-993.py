# Cousins in Binary Tree

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        def depth(node:TreeNode, k:int) -> int:
            queue = deque([node])
            count = 0
            while queue:
                n = len(queue)
                count += 1
                for _ in range(n):
                    node = queue.popleft()
                    if node.val == k:
                        return count
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

        def parent(node:TreeNode, k:int) -> int:
            queue = deque([node])
            while queue:
                n = len(queue)
                for _ in range(n):
                    parent = queue.popleft()
                    if parent.left:
                        if parent.left.val == k:
                            return parent.val
                        queue.append(parent.left)
                    if parent.right:
                        if parent.right.val == k:
                            return parent.val
                        queue.append(parent.right)

        return depth(root,x) == depth(root,y) and parent(root,x) != parent(root,y)