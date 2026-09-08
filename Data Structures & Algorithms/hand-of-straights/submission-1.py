class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)
        for k in counter:
            if k - 1 in counter:
                continue
            
            tmp = k
            while tmp in counter:
                v = counter[tmp]
                if v > 0:
                    for i in range(tmp, tmp + groupSize):
                        if counter[i] < v:
                            return False
                        counter[i] -= v
                tmp += 1
        
        return True
            