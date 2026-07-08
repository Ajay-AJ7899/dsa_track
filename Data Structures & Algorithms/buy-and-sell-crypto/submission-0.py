class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float('inf') #min observed
        maxx = 0 #maxx observed
        for i in prices: #for every iteration
            minn = min(minn,i) #see the min
            diff = i - minn #if stock is sold today 
            maxx = max(diff,maxx) #see the max out of diff and maxx(PREV)
        return maxx