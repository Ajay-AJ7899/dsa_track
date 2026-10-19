class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        dist = [[-1]*cols for _ in range(rows)] #for storing the distance
    
        #calculating the zeros 
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    dist[i][j]=0
                    queue.append((i,j))

        #now need to explore down,up,right,left
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while queue: #bfs code
            r,c = queue.popleft()
            for dr,dc in directions:
                nr = dr+r #new row
                nc = dc+c#new col
            #Before accessing dist[nr][nc], we must check two things:
#1. Is the neighbor inside the matrix boundaries?
#2. Has the neighbor already been visited?
                if nr<0 or nr>= rows or nc <0 or nc>=cols:
                    continue
                if dist[nr][nc]!=-1:
                    continue
                dist[nr][nc] = dist[r][c]+1 #current cell distance +1
                queue.append((nr,nc))
        return dist