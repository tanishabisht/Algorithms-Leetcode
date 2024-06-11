class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l1, l2 = [], []
        for n in nums:
            if n & 1 == 1:
                l1.append(n)
            else:
                l2.append(n)
        return l2 + l1