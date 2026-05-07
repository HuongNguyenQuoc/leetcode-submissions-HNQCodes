class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph:
            graph[src].sort(reverse = True)

        #JFK: ATL, SFO -> SFO, ATL

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            route.append(airport)
            
        dfs("JFK")
        
        return route[::-1]
         