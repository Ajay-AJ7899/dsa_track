class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1] * (n+1)
        dp[0]=0
        two,three = float('inf'),float('inf')
        for i in range(1,n+1):
            one=dp[i-1]+costs[i-1]+1**2
            if i>=2:
               two=dp[i-2]+costs[i-1]+2**2
            if i>=3:
                three=dp[i-3]+costs[i-1]+3**2
            dp[i]= min(one,two,three)
        return dp[n]