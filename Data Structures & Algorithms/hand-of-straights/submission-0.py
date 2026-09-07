class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        for k in sorted(counter):
            n = counter[k]
            if n > 0:
                for i in range(k, k + groupSize):
                    if counter[i] < n:
                        return False
                    counter[i] -= n
        
        return True
