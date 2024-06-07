# Find the K-or of an Array

# Method 1 - Slower
class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        res = 0

        for i in range(32):
            count = 0

            for j in range(len(nums)):
                if nums[j] & 1 == 1:
                    count += 1
                nums[j] = nums[j]>>1

            if count >= k:
                res += 2**i

        return res
    


# Method 2 - Faster
def findKOr(self, nums: List[int], k: int) -> int:

    res = 0

    for i in range(32):
        count = 0

        for j in range(len(nums)):
            if (nums[j]>>i) & 1:
                count += 1

        if count >= k:
            res |= 1<<i

    return res