class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        has={}
        for i,n in enumerate(nums):
            diff = target-n # n is value bez in enumearate it teakes index,value
            if diff in has:
                return [has[diff],i]
            else:
                has[n] = i