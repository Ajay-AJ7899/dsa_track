class Solution:
    def rob(self, nums: list[int]) -> int:
        # [1,2,3,4,5]
        n = len(nums)
        prev = nums[0]
        prev2 = 0
        for i in range(1,n):
            if i>1:
                pick = nums[i]+prev2
            else:
                pick = nums[i]
            notpick = 0+prev
            curr = max(pick,notpick)
            prev2 = prev
            prev = curr
        return prev
