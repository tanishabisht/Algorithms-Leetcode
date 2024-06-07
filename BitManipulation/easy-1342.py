class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        
        while num:
            if num & 1 == 1:
                num -= 1
            else:
                num = num>>1
            count += 1

        return count