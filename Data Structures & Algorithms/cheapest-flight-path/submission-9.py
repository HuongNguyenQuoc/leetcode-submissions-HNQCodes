from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize all prices to infinity, except the starting city
        prices = [float("inf")] * n
        prices[src] = 0
        
        # Iterate exactly k + 1 times (for k stops)
        for _ in range(k + 1):
            # Create a copy to prevent cascaded updates within the same iteration
            tmpPrices = prices.copy()
            
            # Relax all edges
            for u, v, price in flights:
                # If the source node 'u' has been reached, check if this flight is cheaper
                if prices[u] != float("inf") and prices[u] + price < tmpPrices[v]:
                    tmpPrices[v] = prices[u] + price
            
            # Update the main prices array for the next iteration
            prices = tmpPrices
            
        # If the destination price is still infinity, it's unreachable within k stops
        return prices[dst] if prices[dst] != float("inf") else -1