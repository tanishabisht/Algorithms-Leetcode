# Convert a Number to Hexadecimal

def positiveHex(n:int) -> str:
    hexnumber = '0123456789abcdef'
    res = ""
    while n > 0:
        res += hexnumber[n%16]
        n //= 16
    return res[::-1]

def negativeHex(n:int) -> str:
    n = (2**32 + n) & 0xFFFFFFFF
    return positiveHex(n)

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            return negativeHex(num)
        else:
            return positiveHex(num)