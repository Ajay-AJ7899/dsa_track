class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_table = {}
        count = 0
        for i in nums:
            req = k - i
            if req in hash_table and hash_table[req]>0:
                count +=1
                hash_table[req]-=1
            else:
                hash_table[i]= hash_table.get(i,0)+1
        return count