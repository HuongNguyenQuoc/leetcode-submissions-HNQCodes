class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 2:
            stones.sort()
            first = stones.pop()
            second = stones.pop()
            if first > second:
                stones.append(first - second)
        return stones[0] if len(stones) != 0 else 0