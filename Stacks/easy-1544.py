# Make The String Great

class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()
        for ch in s:
            stack.append(ch)
            if len(stack)>1 and abs(ord(ch) - ord(stack[-2])) == 32:
                stack.pop()
                stack.pop()
        return ''.join(stack)