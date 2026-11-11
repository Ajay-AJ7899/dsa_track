class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n = len(triangle)
        dp = [[None]*n for _ in range(n)] 
        def func(i,j):
            if i == n-1:
                return triangle[i][j]
            if dp[i][j]!=None:
                return dp[i][j]
            dp[i][j]=triangle[i][j]+min(func(i+1,j),func(i+1,j+1))
            return dp[i][j]
        return func(0,0)