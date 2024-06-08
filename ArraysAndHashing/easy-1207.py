# Unique Number of Occurrences

# Method 1
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        seen = set()
        for c in counter.values():
            if c in seen:
                return False
            else:
                seen.add(c)
        return True

# Method 2
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = {}
        for a in arr:
            counter[a] = counter.get(a, 0) + 1
        return len(counter) == len(set(counter.values()))
    
# Method 3 - Fastest 
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter) == len(set(counter.values()))