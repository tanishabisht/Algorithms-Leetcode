# Minimum Common Value

# O(nlogm)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        for n in nums1:
            l, r = 0, len(nums2) - 1
            while l <= r:
                m = (l+r) // 2
                if nums2[m] == n:
                    return n
                elif nums2[m] > n:
                    r = m - 1
                else:
                    l = m + 1
        return -1


# O(m+n)
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return -1