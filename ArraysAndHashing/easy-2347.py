# Best Poker Hand

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:

        if len(set(suits)) == 1:
            return 'Flush'

        if Counter(ranks).most_common()[0][1] == 2:
            return 'Pair'
        
        if Counter(ranks).most_common()[0][1] >= 3:
            return 'Three of a Kind'

        return 'High Card'