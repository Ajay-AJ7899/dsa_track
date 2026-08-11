class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = 0
        li = []
        for i in range(len(candies)):
            maxi = max(candies[i],maxi)
            
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxi:
                li.append(True)
            else:
                li.append(False)
        return li