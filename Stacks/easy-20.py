# Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(', '}':'{', ']':'['}
        stack = deque()
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in '}])' and not stack:
                return False
            elif ch in ')}]' and stack and stack.pop() != mapping[ch]:
                return False
        return len(stack) == 0