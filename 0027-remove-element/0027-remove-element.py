class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        li = []
        for i in nums:
            if i != val:
                li.append(i)
        for i in range(len(li)):
            nums[i]=li[i]
        return len(li)