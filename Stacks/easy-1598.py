# Crawler Log Folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = deque()
        for log in logs:
            if log == '../' and s:
                s.pop()
            elif log == './' or (log == '../' and not s):
                continue
            else:
                s.append(log)
        print(s)
        return len(s)