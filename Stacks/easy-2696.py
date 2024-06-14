# Minimum String Length After Removing Substrings

class Solution:
    def minLength(self, s: str) -> int:
        stack = deque()
        for ch in s:
            stack.append(ch)
            if len(stack)>1 and ((stack[-1]=='B' and stack[-2]=='A') or (stack[-1]=='D' and stack[-2]=='C')):
                stack.pop()
                stack.pop()
        return len(stack)