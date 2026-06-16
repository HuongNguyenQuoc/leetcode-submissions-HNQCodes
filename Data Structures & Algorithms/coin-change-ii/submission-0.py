class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for current_coin in range(coin, amount + 1):
                dp[current_coin] += dp[current_coin - coin]
        
        return dp[amount]