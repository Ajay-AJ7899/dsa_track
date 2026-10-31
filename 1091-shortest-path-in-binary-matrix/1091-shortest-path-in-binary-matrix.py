class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0]==1:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        distt = [[sys.maxsize for _ in range(cols)] for _ in range(rows)]
        distt[0][0]=1

        queue = deque()
        queue.append([1,0,0])
        while len(queue)!=0:
            dist,i,j = queue.popleft()
            for x,y in [[1,0],[0,-1],[-1,0],[0,1],[-1,-1],[1,1],[1,-1],[-1,1]]:
                ni, nj = i+x,j+y
                if ni <0 or ni>=rows or nj<0 or nj>=cols:
                    continue
                if grid[ni][nj]==1:
                    continue
                dist_trav = dist+1
                if dist_trav <distt[ni][nj]:
                    distt[ni][nj]=dist_trav
                    queue.append([dist_trav,ni,nj])
        if distt[rows-1][cols-1]==sys.maxsize:
            return -1
        return distt[rows-1][cols-1]