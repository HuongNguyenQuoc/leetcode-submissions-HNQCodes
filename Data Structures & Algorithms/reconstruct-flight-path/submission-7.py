class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)

        for src in graph:
            graph.sort(reverse = True)

        #JFK: ATL, SFO -> SFO, ATL

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

        dfs("JFK")
        
        return route[::-1]
         