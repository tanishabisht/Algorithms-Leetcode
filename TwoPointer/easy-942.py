# DI String Match

# Method 1
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        count, high, ans = 0, len(s), []

        for i in s:
            if i == 'I':
                ans.append(count)
                count += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(count)
        return ans
    

# Method 2
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        count, high, ans = 0, len(s), []
        for i in s:
            if i == 'I':
                ans.append(count)
                count += 1
            else:
                ans.append(high)
                high -= 1
        return ans + [count]
    

# Note: ans + [num] is faster than append as a single operation 
# Append is faster than ans + [num] in case there is a loop