class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        req = 0
        maxi = 0
        for i in gain:
            req = req + i
            maxi = max(maxi,req)
        return maxi