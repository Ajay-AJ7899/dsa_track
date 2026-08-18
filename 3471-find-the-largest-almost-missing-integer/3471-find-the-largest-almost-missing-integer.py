class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        maxi = -1
        hash_map = {}
        for left in range(n - k + 1):
            right = left + k

            # Set removes duplicates inside this window
            window = set(nums[left:right])

            # Count how many windows contain each number
            for x in window:
                hash_map[x] = hash_map.get(x, 0) + 1

                
        for x in hash_map:
            if hash_map[x] ==1:
                maxi = max(maxi,x)
        return maxi