class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        price = [float('inf')] * n
        price[src] = 0

        for _ in range(k + 1):
            tmp = price.copy()

            for s, d, p in flights:
                if price[s] != float('inf') and price[s] + p < tmp[d]:
                    tmp[d] = price[s] + p
                
            price = tmp
        
        return price[dst] if price[dst] != float('inf') else -1
