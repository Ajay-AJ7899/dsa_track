class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def dfs(i,j):
            if i<0 or j<0 or i>= rows or j>=cols:
                return False
            if grid[i][j]==1:
                return True
            grid[i][j]=1#marked visited

            a=dfs(i+1,j)
            b=dfs(i,j+1)
            c=dfs(i-1,j)
            d=dfs(i,j-1)
            return a and b and c and d
        rows = len(grid)
        cols = len(grid[0])
        adj = [[0] * cols for _ in range(rows)]
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0 and adj[i][j]==0:
                    if dfs(i,j):
                        count +=1
        return count 
