# Fair Candy Swap

# O(m*n)
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        a_tot_size = sum(aliceSizes)
        b_tot_size = sum(bobSizes)
        tot = (a_tot_size + b_tot_size) // 2
        for a_curr_size in aliceSizes:
            if tot - (a_tot_size - a_curr_size) in bobSizes:
                return [a_curr_size, tot - (a_tot_size - a_curr_size)]