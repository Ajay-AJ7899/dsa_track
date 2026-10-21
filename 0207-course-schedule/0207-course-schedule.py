class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #in result check whether the len(result)!=numCourses
        #we are doing here using the bfs 
        adj_list = [[] for _ in range(numCourses)]
        result = []
        queue = deque()
        indegree = [0]*numCourses

        #cal the inorder and adj matrix
        for u,v in prerequisites:
            adj_list[u].append(v)
            indegree[v]+=1
        
        #push the 0 degree to the queue
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)

        #khans algo 
        while queue: #while len(queue)>0
            e = queue.popleft()
            result.append(e)

            for i in adj_list[e]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)

        return len(result)==numCourses