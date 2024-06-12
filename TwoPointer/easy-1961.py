# Check If String Is a Prefix of Array

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        wid = 0
        while i < len(s) and wid < len(words):
            print(s[i:], words[wid])
            if s[i:].startswith(words[wid]):
                i += len(words[wid])
                wid += 1
            else:
                return False
        return i >= len(s)