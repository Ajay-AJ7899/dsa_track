class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        median = nums[mid]
        move = 0
        for i in range(len(nums)):
            move += abs(nums[i] - median)
        return move