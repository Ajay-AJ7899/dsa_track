class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        for i in range(0,len(nums)):
            total ^= nums[i]
        if total != 0:
            return len(nums)
        elif any(i!=0 for i in nums):
            return len(nums)-1
        
        else:
            return 0
