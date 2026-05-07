class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in tickets:
            graph[src].append(dst)
        
        for src in graph:
            graph[src].sort(reverse = True)

        stack = ["JFK"]
        route = []

        while stack:
            curr = stack[-1]

            if graph[curr]:
                stack.append(graph[curr].pop())
            
            else:
                route.append(stack.pop())
            
        return route[::-1]



        