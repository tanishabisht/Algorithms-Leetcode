# Minimum Sum of Four Digit Number After Splitting Digits

class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        while num:
            d = num % 10
            digits.append(d)
            num //= 10
        digits.sort()

        num1 = digits[0] * 10 + digits[3] 
        num2 = digits[1] * 10 + digits[2] 

        return num1 + num2