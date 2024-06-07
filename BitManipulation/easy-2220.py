# Minimum Bit Flips to Convert one Number to another

def count_set_bits(num:int) -> int:
    count = 0
    while num:
        num &= num - 1
        count += 1
    return count

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num = start ^ goal
        return count_set_bits(num)