# Reverse String II

# Method 1: inelegant solution
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s) < k:
            return s[::-1]
            
        s = list(s)
        i = 0

        while i+k-1 <= len(s):
            l, r = i, i+k-1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += 2*k

        if i+k-1 > len(s):
            l, r = i, len(s) - 1
            while l < r: 
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)