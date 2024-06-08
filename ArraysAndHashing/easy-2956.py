# Find Common Elements Between Two Arrays

# Method 1
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = Counter(nums1)
        map2 = Counter(nums2)
        common = [k for k in (map1 & map2).keys()]

        ans1, ans2 = 0, 0
        for c in common:
            ans1 += map1[c] 
            ans2 += map2[c]

        return [ans1, ans2]
    

# Method 2: In theory is should be faster but the above is faster for some reason in Leetcode
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = Counter(nums1)
        map2 = Counter(nums2)
        common = map1 & map2

        ans1, ans2 = 0, 0
        for c in common:
            ans1 += map1[c] 
            ans2 += map2[c]

        return [ans1, ans2]