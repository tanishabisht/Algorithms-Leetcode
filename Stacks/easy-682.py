# Baseball Game

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = deque()
        for op in operations:
            if op == '+':
                s.append(s[-1] + s[-2])
            elif op == 'D':
                s.append(2 * s[-1])
            elif op == 'C':
                s.pop()
            else:
                s.append(int(op))
        return sum(s)