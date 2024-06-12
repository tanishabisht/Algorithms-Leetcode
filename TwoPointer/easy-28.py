# Find the Index of the First Occurrence in a String

# Inbuilt function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
# using 2 pointers
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        h, n =len(haystack), len(needle)
        while i<h:
            if haystack[i] == needle[j]:
                if needle[:] == haystack[i:i+n]:
                    return i
            i += 1
        return -1