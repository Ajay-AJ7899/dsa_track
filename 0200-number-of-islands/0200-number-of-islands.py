class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r<0 or r>= rows or c<0 or c>= cols:
                return
            if grid[r][c]=="0" or visited[r][c]==1:
                return
            visited[r][c]=1
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]* cols for _ in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and visited[i][j]==0:
                    count +=1
                    dfs(i,j)
        
        return count
