# Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        l, r = 0, num
        while l <= r:
            m = (l+r) >> 1
            if m * m == num:
                return True
            elif m * m > num:
                r = m - 1
            else:
                l = m + 1
        return False