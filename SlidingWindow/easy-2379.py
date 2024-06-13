# Minimum Recolors to Get K Consecutive Black Blocks

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, k-1
        curr_ops = min_ops = blocks[l:r+1].count('W')
        while r < len(blocks) - 1:
            if blocks[r+1] == 'W' and blocks[l] == 'B':
                curr_ops += 1
            elif blocks[r+1] == 'B' and blocks[l] == 'W':
                curr_ops -= 1
                min_ops = min(min_ops, curr_ops)
            r += 1
            l += 1
        return min_ops