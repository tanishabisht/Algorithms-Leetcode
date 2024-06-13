# Substrings of Size Three with Distinct Characters

# 1st try
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)-2):
            if len(set(s[i:i+3])) == 3:
                count += 1
        return count
    

# 2nd try: using sliding window for generic size n not 3
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        l, r = 0, 2
        seen = Counter(s[l:r+1])
        while r < len(s) - 1:
            
            if len(seen) == 3:
                count += 1

            if seen[s[l]] > 1:
                seen[s[l]] -= 1
            else:
                del seen[s[l]]
            
            seen[s[r+1]] = seen.get(s[r+1], 0) + 1

            l += 1
            r += 1
        return count + 1 if len(seen) == 3 else count 