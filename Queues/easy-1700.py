# Number of Students Unable to Eat Lunch

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        q = deque(students)
        s = deque(sandwiches[::-1])
        while s and s[-1] in q:
            if q[0] == s[-1]:
                q.popleft()
                s.pop()
            elif q[0] != s[-1]:
                first = q.popleft()
                q.append(first)
        return len(s)