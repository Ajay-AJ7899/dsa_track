class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0 
        minn = float('inf')
        for i in prices:
            minn = min(minn,i)
            profit = i - minn
            maxx = max(profit,maxx)
        return maxx