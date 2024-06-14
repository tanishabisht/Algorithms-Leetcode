# Remove Outermost Parentheses

# Using 2 stacks
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        out_stack = deque()
        in_stack = deque()
        res = ''
        for ch in s:
            if ch == '(' and len(out_stack) == 0:
                out_stack.append(ch)
            elif ch == '(' and len(out_stack) != 0:
                in_stack.append(ch)
                res += ch
            elif ch == ')' and len(in_stack) == 0:
                out_stack.pop()
            elif ch == ')' and len(in_stack) != 0:
                res += ch
                in_stack.pop()
        return res