class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {i:[] for i in range(numCourses)}
        idg = [0] * numCourses

        for k, v in prerequisites:
            dic[v].append(k)
            idg[k] += 1
        
        q = deque()
        for i in range(numCourses):
            if idg[i] == 0:
                q.append(i)
        
        finishied = 0
        while q:
            cur = q.popleft()
            finishied += 1

            for pre in dic[cur]:
                idg[pre] -= 1
                if idg[pre] == 0:
                    q.append(pre)
            
        return finishied == numCourses