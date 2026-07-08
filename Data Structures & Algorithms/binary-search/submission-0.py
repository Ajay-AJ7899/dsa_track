class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #sorted and to make in o(logn) use binary search
        l = len(nums)
        low,high = 0,l-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid - 1
        return -1