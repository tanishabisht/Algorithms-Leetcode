# Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        square = n
        seen = set()
        while square != 1:
            n = square
            square = 0
            while n:
                d = n % 10
                n = n // 10
                square += d ** 2
            if square in seen:
                return False
            else:
                seen.add(square)
        return True