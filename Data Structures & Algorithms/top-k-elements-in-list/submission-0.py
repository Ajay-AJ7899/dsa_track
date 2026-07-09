class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ha={}
        for i in nums:
            if i in ha:
                ha[i]+=1
            else:
                ha[i]=1
        sort= sorted(ha.items(), key = lambda x:x[1],reverse = True)
        sort[:k]
        ans = []
        for num,freq in sort[:k]:
            ans.append(num)
        return ans