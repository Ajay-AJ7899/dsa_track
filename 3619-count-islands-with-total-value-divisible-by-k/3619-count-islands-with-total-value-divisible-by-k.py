class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        def dfs(r,c):
            if r <0 or c<0 or r>= rows or c>= cols:
                return 0
            if grid[r][c]==0 or vis[r][c]!=0:
                return 0
            vis[r][c]=1 #assign
            total = grid[r][c]
            total += dfs(r+1,c)
            total += dfs(r,c+1)
            total += dfs(r-1,c)
            total += dfs(r,c-1)
            return total
        rows = len(grid)
        cols = len(grid[0])
        vis = [[0]*cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]!=0 and not vis[i][j]:
                    a=dfs(i,j)
                    if a%k ==0:
                        count+=1
        return count
        