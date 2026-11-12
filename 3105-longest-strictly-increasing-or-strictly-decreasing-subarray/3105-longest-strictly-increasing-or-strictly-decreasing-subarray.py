class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = incr = dec = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                incr+=1
                dec = 1
            elif nums[i]<nums[i-1]:
                dec +=1
                incr = 1
            else:
                incr = dec = 1
            ans = max(ans,incr,dec)
        return ans