class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        def func(i,j):
            if i<0 or j<0:
                return float('inf')
            if i ==0 and j ==0 :
                return grid[0][0]
            if dp[i][j]!= -1:
                return dp[i][j]
            dp[i][j]= grid[i][j]+min(func(i-1,j),func(i,j-1))
            return dp[i][j]
        return func(m-1,n-1)