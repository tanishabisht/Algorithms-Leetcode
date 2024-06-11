# Sort Array By Parity II

# Method 1: 2 * O(N)
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd, even, ans = [], [], []

        for n in nums:
            if n & 1 == 1:
                odd.append(n)
            else:
                even.append(n)

        o, e = 0, 0
        for i in range(len(nums)):
            if i & 1 == 1:
                ans.append(odd[o])
                o += 1
            else:
                ans.append(even[e])
                e += 1

        return ans
        

# Method 2: O(n)

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        e, o = 0, 1

        for n in nums:
            if n & 1 == 1:
                ans[o] = n
                o += 2
            else:
                ans[e] = n
                e += 2

        return ans