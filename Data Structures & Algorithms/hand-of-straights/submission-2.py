class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        # The idea is we can follow the first value in each chain by check k - 1 whether the in counter and if not absolutely current value is first of each chain
        counter = Counter(hand)
        for k in counter:
            if k - 1 in counter:
                continue
            
            tmp = k # Use tmp variable so we can continue check tmp in counter
            while tmp in counter:
                v = counter[tmp] # n here means number of group we need create continuous v group at head chain 
                if v > 0:
                    for i in range(tmp, tmp + groupSize):
                        if counter[i] < v:
                            return False
                        counter[i] -= v # We have minus the number of v at each key
                tmp += 1
        
        return True
            