class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i: int, holding: bool) -> int:
            if i >= len(prices):
                return 0
            
            if holding:
                #Option 1: sell today
                sell = prices[i] + dfs(i + 2, False)

                #Option 2: do nothing
                skip = dfs(i + 1, True)

                return max(sell, skip)
            
            else:
                #Option 1: buy today
                buy = -prices[i] + dfs(i + 1, True)

                #Option 2: do nothing
                skip = dfs(i + 1, False)
            
                return max(buy, skip)
        
        return dfs(0, False)