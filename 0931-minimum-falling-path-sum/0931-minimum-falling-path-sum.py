class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[None]*rows for _ in range(cols)]
        def func(i,j):
          #falling min path
            if j<0 or j>=n:
                return float('inf')
            if i == n-1:
                return matrix[i][j]
            if dp[i][j]!=None:
                return dp[i][j]
            dp[i][j]= matrix[i][j]+min(func(i+1,j+1), func(i+1,j), func(i+1,j-1))
            return dp[i][j]
        ans = float('inf')
        for col in range(n):
            ans = min(ans,func(0,col))
        return ans