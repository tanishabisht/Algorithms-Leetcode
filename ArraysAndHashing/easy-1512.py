# Number of Good Pairs 1

# Method 1: slowest
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)

        res = 0
        for v in counts.values():
            if v > 1:
                res += (v * (v-1)) // 2
        
        return res

# Method 2: From method 1 removed the if statement as it is not useful 
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)

        res = 0
        for v in counts.values():
            res += (v * (v-1)) // 2
        
        return res
    
# Method 3: Formula change using combinatorics
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)

        res = 0
        for v in counts.values():
            res += math.comb(n, 2)
        
        return res
    

# Method 4: Formula change using combinatorics - compact array
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(math.comb(v, 2) for v in counts.values())