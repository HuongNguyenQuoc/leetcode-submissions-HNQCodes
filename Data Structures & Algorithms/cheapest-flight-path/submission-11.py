class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmpPrices = prices.copy()
            
            for s, d, p in flights: #s: source, d: destination, p: price
                if prices[s] != float('inf') and prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            
            prices = tmpPrices
         
        return prices[dst] if prices[dst] != float('inf') else -1