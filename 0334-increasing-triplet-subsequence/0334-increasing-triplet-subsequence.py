class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x,y = float('inf'),float('inf')
        for i in nums:
            if x>=i:
                x = i
            elif y>=i:
                y = i
            else:
                return True
        return False
           