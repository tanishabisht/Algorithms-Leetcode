# Maximum Odd Binary Number

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = sum([i=='1' for i in s])
        zeros = len(s) - ones
        return "1"*(ones - 1) + "0"*zeros + "1"