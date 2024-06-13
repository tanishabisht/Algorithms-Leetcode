# Find the K-Beauty of a Number

# 1st Try
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num = str(num)
        l, r = 0, k-1
        count = 0

        while r < len(num):
            n = int(num[l:r+1])
            if n!=0 and int(num) % n == 0:
                count += 1
            r += 1
            l += 1

        return count