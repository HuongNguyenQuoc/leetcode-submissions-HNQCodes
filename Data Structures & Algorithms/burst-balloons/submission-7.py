class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ballons = [1] + nums + [1]
        n = len(ballons)
        memo = {}

        def dp(left: int, right: int) -> int:
            if left + 1 == right:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            
            best = 0
            for k in range(left + 1, right):
                coins = ballons[left] * ballons[k] * ballons[right]
                total = dp(left, k) + dp(k, right) + coins
                best = max(best, total)
            
            memo[(left, right)] = best
            return best

        return dp(0, n - 1)