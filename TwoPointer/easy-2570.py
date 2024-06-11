# Merge Two 2D Arrays by Summing Values

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dict1 = Counter({k:v for [k,v] in nums1})
        dict2 = Counter({k:v for [k,v] in nums2})
        dictRes = dict1 + dict2
        ans = [[k,v] for k,v in dictRes.items()]
        ans.sort()
        return ans