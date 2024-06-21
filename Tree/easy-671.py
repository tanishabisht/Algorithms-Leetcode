# Second Minimum Node In a Binary Tree

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        seen = set()

        def dfs(node:TreeNode) -> None:
            if not node: return None
            seen.add(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        seen_list = list(seen)
        seen_list.sort()
        return seen_list[1] if len(seen_list) > 1 else -1