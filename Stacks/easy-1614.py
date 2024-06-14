# Maximum Nesting Depth of the Parentheses

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = deque()
        size = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')':
                size = max(size, len(stack))
                stack.pop()
        return size