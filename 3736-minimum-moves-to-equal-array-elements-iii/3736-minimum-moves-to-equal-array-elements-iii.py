class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        move = 0
        for i in range(len(nums)):
            move+=maxi-nums[i]
        return move