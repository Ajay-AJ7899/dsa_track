class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hash = {}
        for i in range(len(arr)):
            hash[arr[i]]=hash.get(arr[i],0)+1
        # if multiple like 1-2, 2-2 times repeated then in set wala only 2 is conidered which means len(2)- 1 == len(1,2) --- 1==2 false 
        return len(set(hash.values()))== len(hash.values())