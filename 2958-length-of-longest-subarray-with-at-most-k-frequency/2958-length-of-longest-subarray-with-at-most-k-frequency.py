class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0 
        freq = {}
        maxi = 0
        for right in range(len(nums)):
            freq[nums[right]] = freq.get(nums[right],0)+1
            while freq[nums[right]]>k:
                freq[nums[left]]-=1
                left +=1
            maxi = max(maxi,right-left+1) #return length of subarray
        return maxi