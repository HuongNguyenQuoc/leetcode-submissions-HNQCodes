class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        for node in graph:
            graph[node].sort(reverse = True)
            
        stack = ["JFK"]
        res = []

        while stack:
            curr = stack[-1]
            if not graph[curr]:
                res.append(stack.pop())
            else:
                stack.append(graph[curr].pop())
        
        return res[::-1]