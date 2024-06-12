# Check If N and Its Double Exist

# Method 1: not so elegant soln
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set(arr)
        zeros = len([n for n in arr if n == 0])

        if zeros == 1:
            for num in arr:
                if num!=0 and (num*2 in seen or num/2 in seen):
                    return True
            return False
        elif zeros == 0:
            for num in arr:
                if num*2 in seen or num/2 in seen:
                    return True
            return False
        else:
            return True
        
# Method 2 - same time but more elegant solution
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1: return True
        seen = set(arr) - {0}

        for num in arr:
            if num*2 in seen:
                return True
        return False