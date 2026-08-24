class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        ballons = [1] + nums + [1]
        n = len(ballons)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                for k in range(left + 1, right):
                    coins = ballons[left] * ballons[k] * ballons[right]
                    coins += dp[left][k] + dp[k][right]
                    dp[left][right] = max(dp[left][right], coins)
        
        return dp[0][n - 1]