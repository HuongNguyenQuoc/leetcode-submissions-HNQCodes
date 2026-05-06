class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)
        
        for airport in graph:
            graph[airport].sort(reverse = True)
        
        #JFK: ATL, SFO -> SFO, ATL
        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            
            route.append(airport)

        dfs("JFK")
        return route[::-1]