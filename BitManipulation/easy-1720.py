# Decode XORed Array

# Method 1 - slower
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [0]*(len(encoded)+1)
        decoded[0] = first

        for i in range(len(encoded)):
            decoded[i+1] = encoded[i] ^ decoded[i]

        return decoded 
    
# Method 2 - Faster
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]

        for i in range(len(encoded)):
            decoded.append(encoded[i] ^ decoded[i])

        return decoded