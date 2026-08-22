class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ballons = [1] + nums + [1]
        n = len(ballons)
        dp = {}

        def resolve(left: int, right: int) -> int:
            if right - left < 2:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            
            best = 0
            for k in range(left + 1, right):
                coins = ballons[left] * ballons[k] * ballons[right]
                total = resolve(left, k) + resolve(k, right) + coins

                if total > best:
                    best = total
            
            dp[(left, right)] = best
            return best

        return resolve(0, n - 1)