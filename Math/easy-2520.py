# Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:
        digits = [int(i) for i in str(num)]
        count = 0
        for d in digits:
            if num % d == 0:
                count += 1
        return count
        