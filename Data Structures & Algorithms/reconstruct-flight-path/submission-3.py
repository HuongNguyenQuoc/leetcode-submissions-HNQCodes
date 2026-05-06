class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        route = []

        for airport in graph:
            graph[airport].sort(reverse=True)

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            route.append(airport)

        dfs('JFK')

        return route[::-1]