from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Build graph
        for src, dst in tickets:
            graph[src].append(dst)

        # Sort destinations in reverse order
        # So we can pop from the end efficiently
        for src in graph:
            graph[src].sort(reverse=True)

        route = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            route.append(airport)

        dfs("JFK")

        return route[::-1]