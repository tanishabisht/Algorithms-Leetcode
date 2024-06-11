# Merge Strings Alternately

# Mehtod 1: two pointer
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j, ans = 0, 0, ""

        while i < len(word1) and j < len(word2):
            ans += word1[i] + word2[j]
            i += 1
            j += 1
        
        while i < len(word1):
            ans += word1[i]
            i += 1

        while j < len(word2):
            ans += word2[j]
            j += 1

        return ans