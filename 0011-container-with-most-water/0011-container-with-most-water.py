class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height)-1
        n = len(height)
        maxi = 0
        while (i<j):
            h = min(height[i],height[j])
            w = j-i
            water = h*w
            maxi = max(water,maxi)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return maxi