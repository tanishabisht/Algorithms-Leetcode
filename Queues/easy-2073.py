# Time Needed to Buy Tickets

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        ans = 0
        for i,v in enumerate(tickets):
            q.append([i,v])
        while q:
            first = q.popleft()
            if first[0] == k and first[1] == 1:
                return ans + 1
            if first[1] > 1:
                q.append([first[0], first[1] - 1])
            ans += 1