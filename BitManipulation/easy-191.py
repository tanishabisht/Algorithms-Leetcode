# Number of 1 Bits

# Brian Kernighan's Algorithm
# Hamming Weight: refers to the number of symbols that are different from the zero-symbol in a string

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count