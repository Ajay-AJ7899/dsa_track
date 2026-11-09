class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]* n for _ in range(m)]
        def func(i, j):

            if i < 0 or j < 0:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0

            if i == 0 and j == 0:
                return 1
            
            if dp[i][j]!=-1:
                return dp[i][j]
        
            dp[i][j] = func(i-1,j)+func(i,j-1)
            return dp[i][j]

        return func(m - 1, n - 1)