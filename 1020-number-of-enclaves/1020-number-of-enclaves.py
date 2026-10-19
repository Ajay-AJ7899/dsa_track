class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        count = 0
        def dfs(r,c):
            #edge cases
            if r<0 or r>= rows or c<0 or c>= cols:
                return 
            if grid[r][c]== 0 or visited[r][c]==1:
                return 
            visited[r][c]=1
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)

        rows = len(grid)
        cols = len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if i ==0 or j == 0 or i == rows-1 or j == cols-1:
                    if grid[i][j]==1:
                        dfs(i,j)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]!= 0 and visited[r][c]==0:
                    count +=1
        return count