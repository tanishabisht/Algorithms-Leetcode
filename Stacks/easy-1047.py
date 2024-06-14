# Remove All Adjacent Duplicates In String

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for ch in s:
            stack.append(ch)
            if len(stack)>1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
        return "".join(stack)
        