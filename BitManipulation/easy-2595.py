# Number of Even and Odd Bits

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd, even = 0, 0

        for i in range(32):

            if n & 1:
                print(n, i)
                if i & 1 == 1:
                    odd += 1
                else:
                    even += 1

            n = n >> 1

        return [even, odd]
        