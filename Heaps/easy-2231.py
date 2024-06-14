# Largest Number After Digit Swaps by Parity

class Solution:
    def largestInteger(self, num: int) -> int:
        num = [int(n) for n in list(str(num))]
        oddList = [-n for n in num if n&1 == 1]
        odd = oddList[:]
        evenList = [-n for n in num if n&1 == 0]
        even = evenList[:]

        heapq.heapify(odd)
        heapq.heapify(even)

        res = []
        for n in num:
            if -n in oddList:
                res.append(-heapq.heappop(odd))
            elif -n in evenList:
                res.append(-heapq.heappop(even))
        return int(''.join([str(i) for i in res]))