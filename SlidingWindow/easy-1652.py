# Defuse the Bomb

# 1st try
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0]*len(code)

        if k > 0:
            l, r = 1, k
            next_sum = sum(code[l:r+1])
            i = 0
            decode = [0]*len(code)
            n = len(code)
            while i < len(code):
                decode[i] = next_sum
                next_sum += code[(r+1)%n] - code[l%n]
                i += 1
                l += 1
                r += 1
            return decode

        if k < 0:
            l, r = len(code) + k - 1, len(code) - 2
            prev_sum = sum(code[l:r+1])
            i = len(code) - 1
            decode = [0]*len(code)
            n = len(code)
            while i >= 0:
                decode[i] = prev_sum
                prev_sum += code[(l-1)%n] - code[r%n]
                i -= 1
                l -= 1
                r -= 1
            return decode