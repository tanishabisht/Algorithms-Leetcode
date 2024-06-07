# Sort Integers by The Number of 1 Bits

def count_set_bits(n:int) -> int:
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        sorted_data = sorted(arr, key=lambda n: (count_set_bits(n), n))
        return sorted_data