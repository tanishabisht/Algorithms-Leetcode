# Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        summ = 0
        while n:
            d = n % 10
            prod *= d
            summ += d
            n = n // 10
        return prod - summ