class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)

        for k in counter:
            if k - 1 in counter:
                continue
            
            n = k
            while n in counter:
                v = counter[n]
                if v > 0:
                    for i in range(n, n + groupSize):
                        if counter[i] < v:
                            return False
                        counter[i] -= v
                n += 1
            
        return True
