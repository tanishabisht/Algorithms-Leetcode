# Find First Palindromic String in the Array

# Method 1
def isPalindrome(s:str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if isPalindrome(word):
                return word
        return ""
    

# Method 2 - Faster
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""