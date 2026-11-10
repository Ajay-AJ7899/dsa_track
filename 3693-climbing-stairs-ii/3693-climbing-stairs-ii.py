class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [-1] * (n+1)
        def func(i):
            if i == 0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            one = func(i-1) + costs[i-1] + 1**2

            two = float('inf')
            if i >= 2:
                two = func(i-2) + costs[i-1] + 2**2

            three = float('inf')
            if i >= 3:
                three = func(i-3) + costs[i-1] + 3**2

            dp[i]= min(one, two, three)
            return dp[i]
        return func(n)