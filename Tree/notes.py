from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_dfs_recursive(node:TreeNode) -> None:
    if node:
        print(node.val)
        preorder_dfs_recursive(node.left)
        preorder_dfs_recursive(node.right)

def inorder_dfs_recursive(node:TreeNode) -> None:
    if node:
        inorder_dfs_recursive(node.left)
        print(node.val)
        inorder_dfs_recursive(node.right)

def postorder_dfs_recursive(node: TreeNode) -> None:
    if node:
        postorder_dfs_recursive(node.left)
        postorder_dfs_recursive(node.right)
        print(node.val)

def preorder_dfs_iterative(root: TreeNode) -> None:
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


def inorder_dfs_iterative(root: TreeNode) -> None:
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node.left)
        node = stack.pop()
        print(node.val)
        node = node.right


def postorder_dfs_iterative(root: TreeNode) -> None:
    stack1 = [root]
    stack2 = []
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        print(node.val)


def bfs_iterative(root: TreeNode) -> None:
    queue = deque([root])
    while queue:
        n = len(queue)
        for _ in range(n):
            node = queue.popleft()
            print(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



# 543. Diameter of Binary Tree
# 101. Symmetric Tree
# 110. Balanced Binary Tree
# 111. Minimum Depth of Binary Tree
# 112. Path Sum
# 572. Subtree of Another Tree
# 703. Kth Largest Element in a Stream
# 108. Convert Sorted Array to Binary Search Tree