# Remove Palindromic Subsequences

def isPalindrom(s:str) -> bool:
    l,r = 0,len(s)-1
    while l<r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if isPalindrom(s) else 2