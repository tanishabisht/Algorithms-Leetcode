# Long Pressed Name

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, t = 0, 0

        if len(typed) < len(name):
            return False

        while t < len(typed):

            if n < len(name) and name[n] == typed[t]:
                n += 1
                t += 1
            
            elif t>0 and typed[t-1]==typed[t]:
                t += 1

            else:
                return False

        return n == len(name)
        