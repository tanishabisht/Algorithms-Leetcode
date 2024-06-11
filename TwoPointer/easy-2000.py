# Reverse Prefix of Word

# Method 1 - reverse string
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        r = word.find(ch)
        if r == -1:
            return word
        return word[r::-1] + word[r+1:]
    
# Method 2 - 2 pointer
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l, r = 0, word.find(ch)
        if r == -1:
            return word

        word = list(word)
        while l < r:
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1

        return ''.join(word)