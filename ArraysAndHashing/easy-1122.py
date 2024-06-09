# Relative Sort Array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_map = {val:pos for pos,val in enumerate(arr2)}
        # This offset=1000 should be larger than any index that an element of arr2 can have.
        res = sorted(arr1, key=lambda n: (arr2_map.get(n, 1000 + n)))
        return res