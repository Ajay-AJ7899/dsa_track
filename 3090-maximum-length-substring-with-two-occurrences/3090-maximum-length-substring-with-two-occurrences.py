class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hash_table = {}
        left = 0
        maxi = 0
        for right in range(len(s)):
            hash_table[s[right]]= hash_table.get(s[right],0)+1
            while hash_table[s[right]]>2:
                hash_table[s[left]]-=1
                left+=1
            maxi = max(maxi, right-left+1)
        return maxi