# Find Smallest Letter Greater Than Target

# O(logn)
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        l, r = 0, len(letters) - 1
        while l <= r:
            m = (l+r) // 2
            if letters[m] == target:
                l = m + 1
            elif letters[m] > target:
                r = m - 1
                ans = letters[m]
            elif letters[m] < target:
                l = m + 1
        return ans
    
# O(logn)
# reducing the number of if elses in the above code
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ans = letters[0]
        l, r = 0, len(letters) - 1
        while l <= r:
            m = (l+r) // 2
            if letters[m] > target:
                r = m - 1
                ans = letters[m]
            else:
                l = m + 1
        return ans