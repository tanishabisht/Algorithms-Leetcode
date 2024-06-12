# Reverse Vowels of a String

class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r, vowel = 0, len(s) - 1, 'aeiou'
        s = list(s)
        while l < r:
            if s[l] in vowel and s[r] in vowel:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] not in vowel:
                l += 1
            elif s[r] not in vowel:
                r -= 1
        return ''.join(s)