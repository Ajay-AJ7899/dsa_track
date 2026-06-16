class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check the length
        if len(s) == len(t):
            if  sorted(s) == sorted(t):
                return True
            else: return False
        else:
            return False


# more effectient way use the hash maps to store the freq of character 
# for i in range(len(s)): counts[s[i]] = counts.get(s[i],0) +1
# countt[t[i]]= countt.get(t[i],0)+1
#return counts==countt

       