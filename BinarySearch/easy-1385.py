# Find the Distance Value Between Two Arrays

# O(n^2)
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for num in arr1:
            if all([abs(num - arr2[i])> d for i in range(len(arr2))]):
                count += 1
        return count
    
# O(nlogn sorting + nlogn)

def binarySearch(nums:List[int], n:int, d:int) -> int:
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l+r) // 2
        if abs(nums[m] - n) <= d:
            return False
        elif nums[m] > n:
            r = m - 1
        else:
            l = m + 1
    return True

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
        for n in arr1:
            if binarySearch(arr2, n, d):
                count += 1
        return count