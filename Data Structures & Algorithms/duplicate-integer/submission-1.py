class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # freq = {}
        # for i in freq:
        #     if i in hash:
        #        freq[i] = freq.get(i, 0) + 1 useful if we need to find the frequency here its duplicate so use set dict

        # or convert to set O(n)
        return len(set(nums))< len(nums) #if yes there is repeat then true else false