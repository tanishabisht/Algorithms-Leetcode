# Maximum Length Substring With Two Occurrences

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hashmap = {}
        l, r = 0, 0
        count = 0
        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            while hashmap[s[r]] > 2:
                if s[l] in hashmap:
                    if hashmap[s[l]] == 1:
                        del hashmap[s[l]]
                    else:
                        hashmap[s[l]] -= 1
                l += 1
            count = max(count, r-l+1)
            r += 1
        return count