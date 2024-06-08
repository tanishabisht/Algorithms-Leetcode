# Find Missing and Repeated Values

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid) * len(grid) 
        flat_grid = list(itertools.chain(*grid))

        repeating = Counter(flat_grid).most_common(1)[0][0]
        missing = (set([i+1 for i in range(n)]) - set(flat_grid)).pop()

        return [repeating, missing]