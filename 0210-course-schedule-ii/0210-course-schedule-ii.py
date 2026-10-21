class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        result = []
        queue = deque()

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1

        #if put all zeros indegree to queue
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        #khans algo 
        while queue:
            e = queue.popleft()
            result.append(e)
            for i in adj[e]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        if len(result)==numCourses:
            return result
        else:
            return []