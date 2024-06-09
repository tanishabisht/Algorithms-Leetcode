# Rank Transform of an Array

# Method 1 - Time exceeded: O(n^2) time complexity
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        ranks = [1]
        rank = 1
        for i in range(1, len(sorted_arr)):
            if sorted_arr[i] != sorted_arr[i-1]:
                rank += 1
                ranks.append(rank)
            else:
                ranks.append(rank)

        res = [ranks[sorted_arr.index(num)] for num in arr]
        return res
    

# Method 2
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(enumerate(arr), key=lambda n: n[1])
        ranks = {}
        rank = 1
        for i, (pos, val) in enumerate(sorted_arr):
            if val not in ranks:
                ranks[val] = rank
                rank += 1
        return [ranks[num] for num in arr]
    
    
# Method 3
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)

        ranks = {}
        rank = 1
        for i in sorted_arr:
            if i not in ranks:
                ranks[i] = rank
                rank += 1
                
        return [ranks[num] for num in arr]