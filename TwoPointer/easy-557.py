# Reverse Words in a String III

# Method 1: 2 pointer
def rev(w:str) -> str:
    l, r = 0, len(w) - 1
    w = list(w)
    while l < r:
        w[l], w[r] = w[r], w[l]
        l += 1
        r -= 1
    return ''.join(w)

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            words[i] = rev(words[i])
        return ' '.join(words)
    
# Method 2: using inverse of a string
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return ' '.join(words)
    

# Method 3: using inverse of a string and a new variable to store answer
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        ans = ""
        for w in words:
            ans += w[::-1] + ' '
        return ans[:-1]