class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left,right = 0, sum(nums)
        for idx, ele in enumerate(nums):
            right -= ele
            if right == left:
                return idx
            left +=ele
        return -1